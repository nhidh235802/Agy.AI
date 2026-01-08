import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector  # Kiểu dữ liệu đặc biệt cho RAG
from app.core.database import Base

# --- ĐỊNH NGHĨA CÁC ENUM (Lựa chọn cố định) ---
class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class UserTier(enum.Enum):
    FREE = "free"
    VIP = "vip"

class TransactionType(enum.Enum):
    DEPOSIT = "deposit"      # Nạp tiền
    BUY_VIP = "buy_vip"      # Mua VIP
    REWARD = "reward"        # Thưởng
    CHECKIN = "checkin"      # Điểm danh

class MessageRole(enum.Enum):
    USER = "user"
    MODEL = "model"

# --- 1. BẢNG USERS (Người dùng) ---
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(200), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    
    # Phân quyền & Hạng
    role = Column(Enum(UserRole), default=UserRole.USER)
    tier = Column(Enum(UserTier), default=UserTier.FREE)
    
    # Kinh tế
    coin_balance = Column(Integer, default=0)
    vip_expires_at = Column(DateTime, nullable=True) # Hết hạn thì về FREE
    
    created_at = Column(DateTime, default=datetime.utcnow)

    # Quan hệ
    bots_created = relationship("Character", back_populates="creator")
    conversations = relationship("Conversation", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")

# --- 2. BẢNG TRANSACTIONS (Giao dịch/Xu) ---
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Integer, nullable=False) # Số dương là cộng, âm là trừ
    transaction_type = Column(Enum(TransactionType), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")

# --- 3. BẢNG CHARACTERS (Nhân vật) ---
class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("users.id")) 
    
    name = Column(String(100), nullable=False)
    avatar_url = Column(Text, nullable=True)
    pronouns = Column(String(50)) # Anh/Em, Ta/Ngươi...
    
    # Các trường Prompting
    personality = Column(Text)
    appearance = Column(Text)
    likes = Column(Text)
    dislikes = Column(Text)
    greeting = Column(Text)
    example_dialogue = Column(Text) # Văn mẫu
    
    # Trường Context Scenario (User: 200 từ, VIP: 500 từ - Logic xử lý ở code)
    context_scenario = Column(Text, nullable=True)
    
    is_public = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    creator = relationship("User", back_populates="bots_created")
    conversations = relationship("Conversation", back_populates="character")
    knowledge_base = relationship("CharacterKnowledge", back_populates="character")

# --- 4. BẢNG KNOWLEDGE (RAG - Trí nhớ dài hạn) ---
class CharacterKnowledge(Base):
    __tablename__ = "character_knowledge"

    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"))
    
    file_name = Column(String(255))
    content_chunk = Column(Text, nullable=False) # Đoạn văn bản gốc
    
    # VECTOR: Đây là điều kỳ diệu. 768 là kích thước vector chuẩn của Google Gemini
    embedding = Column(Vector(768)) 
    
    created_at = Column(DateTime, default=datetime.utcnow)

    character = relationship("Character", back_populates="knowledge_base")

# --- 5. BẢNG CONVERSATIONS (Cuộc hội thoại) ---
class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))
    
    # --- PHẦN BỔ SUNG: USER PERSONA (Dành cho VIP) ---
    user_pronouns = Column(String(50), nullable=True)   
    user_call_me_as = Column(String(50), nullable=True)
    user_age = Column(Integer, nullable=True)
    user_sexual_orientation = Column(String(50), nullable=True)
    user_occupation = Column(String(100), nullable=True)
    user_hobbies = Column(Text, nullable=True)
    user_personality = Column(Text, nullable=True)
    user_likes = Column(Text, nullable=True)
    user_dislikes = Column(Text, nullable=True)
    user_appearance = Column(Text, nullable=True)
    
    last_message_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="conversations")
    character = relationship("Character", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")

# --- 6. BẢNG MESSAGES (Tin nhắn chi tiết) ---
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    
    role = Column(Enum(MessageRole), nullable=False) # 'user' hoặc 'model'
    content = Column(Text, nullable=False)
    
    # Tính năng GHIM tin nhắn (User: 8, VIP: 12)
    is_pinned = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    conversation = relationship("Conversation", back_populates="messages")