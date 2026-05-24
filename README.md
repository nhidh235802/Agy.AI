# Character Chatbot (Gemini API & RAG)

[English](#english) | [Tiếng Việt](#tiếng-việt) | [日本語](#日本語)

---

## English

This is a personal learning project built to practice **Python** backend development and practical **Artificial Intelligence (AI)** application. 

The main objective of this project is to understand how to integrate Large Language Models (LLMs) and work with relational databases combined with vector search to build an interactive roleplay chatbot application.

### 📚 Technologies & Concepts Learned

1. **Python & FastAPI**:
   * Building APIs and handling backend logic.
   * Managing database connections using SQLAlchemy ORM.

2. **Google Gemini API**:
   * Utilizing LLMs to let bots roleplay based on custom personality profiles.
   * Generating vector embeddings from text for semantic searches.

3. **RAG (Retrieval-Augmented Generation)**:
   * Learning how to provide external documents/knowledge to the AI so the chatbot replies accurately based on existing data.

4. **PostgreSQL & pgvector**:
   * Storing user, character, and chat history data.
   * Storing and performing semantic searches using the `pgvector` extension.

### 🌟 Core Features Under Development

* **Custom Character Creation**: Users set personality, pronouns, appearance, and initial greetings for the chatbot.
* **Smart Conversation (RAG)**: Allowing document uploads for characters so they respond based on the provided context.
* **Personalized Chats (User Persona)**: Bots adjust their style and pronouns based on user profiles.
* **Tiered Access Control**: Designing feature limits (messages, context words) between FREE and VIP accounts to practice DB design and authorization logic.

---

## Tiếng Việt

Đây là một dự án cá nhân được xây dựng để học tập và thực hành về lập trình backend với **Python** và ứng dụng **Trí tuệ nhân tạo (AI)** vào thực tế. 

Mục tiêu chính của dự án là hiểu cách tích hợp các mô hình ngôn ngữ lớn (LLMs), làm việc với cơ sở dữ liệu quan hệ kết hợp tìm kiếm vector (Vector Search) để tạo ra một ứng dụng chatbot tương tác.

### 📚 Các Công Nghệ & Khái Niệm Đang Học

1. **Python & FastAPI**:
   * Xây dựng API và xử lý logic phía backend.
   * Quản lý kết nối cơ sở dữ liệu thông qua SQLAlchemy ORM.

2. **Google Gemini API**:
   * Sử dụng mô hình LLM để bot đóng vai (roleplay) theo tính cách nhân vật đã thiết lập.
   * Tạo Vector Embeddings từ văn bản phục vụ cho việc tìm kiếm ngữ nghĩa.

3. **Kỹ thuật RAG (Retrieval-Augmented Generation)**:
   * Tìm hiểu cách cung cấp thêm kiến thức/tài liệu ngoài cho AI để chatbot trả lời chính xác thông tin dựa trên dữ liệu có sẵn.

4. **PostgreSQL & pgvector**:
   * Lưu trữ dữ liệu người dùng, nhân vật và lịch sử chat.
   * Thực hành lưu trữ và tìm kiếm vector (Semantic Search) bằng extension `pgvector`.

### 🌟 Ý Tưởng Tính Năng Đang Phát Triển

* **Tạo nhân vật tùy chỉnh**: Người dùng thiết lập tính cách (personality), danh xưng (pronouns), ngoại hình (appearance) và lời chào ban đầu cho chatbot.
* **Hội thoại thông minh (RAG)**: Cho phép nạp tài liệu cho nhân vật để bot phản hồi dựa trên tài liệu đó.
* **Cá nhân hóa hội thoại (User Persona)**: Bot tự động điều chỉnh cách xưng hô dựa trên thông tin cá nhân của người dùng.
* **Hệ thống phân quyền**: Thiết kế tính năng giới hạn tin nhắn và số lượng từ bối cảnh giữa tài khoản miễn phí (FREE) và trả phí (VIP).

---

## 日本語

このプロジェクトは、**Python**でのバックエンド開発および**人工知能（AI）**の応用を学習・実践するために構築された個人学習用プロジェクトです。

主な目的は、大規模言語モデル（LLM）の統合方法を理解し、ベクトル検索を組み合わせたリレーショナルデータベースを活用してインタラクティブなチャットボットを作成することです。

### 📚 学習している技術・概念

1. **Python & FastAPI**:
   * APIの構築とバックエンドロジックの処理。
   * SQLAlchemy ORMによるデータベース接続管理。

2. **Google Gemini API**:
   * 設定されたキャラクターの性格に基づいて、ボットにロールプレイを行わせる。
   * テキストからベクトル埋め込み（Embeddings）を生成し、セマンティック検索に活用する。

3. **RAG (検索拡張生成)**:
   * 既存のデータに基づいてチャットボットが正確に回答できるよう、外部ドキュメントや知識をAIに提供する方法の学習。

4. **PostgreSQL & pgvector**:
   * ユーザー、キャラクター、チャット履歴の保存。
   * `pgvector` 拡張機能を使用したベクトルの保存と類似性検索（セマンティック検索）の実践。

### 🌟 開発中のコア機能

* **カスタムキャラクター作成**: チャットボットの性格（Personality）、代名詞（Pronouns）、外見（Appearance）、初期の挨拶文を設定可能。
* **スマートな会話 (RAG)**: キャラクターに資料を取り込ませることで、その資料に基づいてボットが回答できるようにする。
* **パーソナライズされた会話 (User Persona)**: ユーザーのプロフィール情報に合わせて、ボットが呼び方や話し方を自動調整する。
* **権限管理システム**: データベース設計と権限ロジックの実践として、一般（FREE）とプレミアム（VIP）アカウント間でのメッセージ制限やコンテキスト文字数の制限を設計。