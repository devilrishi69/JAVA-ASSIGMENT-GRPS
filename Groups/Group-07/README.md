# RuralConnect

> **🌾 Rural Marketplace & Supply Chain Platform**

RuralConnect is a student web application designed to connect rural producers such as farmers, weavers, and artisans with buyers through a digital marketplace.

The project combines a marketplace, buyer and producer dashboards, bulk ordering, order tracking, and an auction/bidding system in one platform.

---

## 👥 Team Members

1. Ayush Kumar
2. Vasudev Choudhary
3. Saumil Kurre
4. Shivam Sharma

---

## 📌 About the Project

RuralConnect provides a simple digital platform where rural producers can list their products and buyers can discover and purchase them.

The project is designed as an academic demonstration of a web-based marketplace and supply-chain system using Java, Apache Tomcat, MySQL, and frontend web technologies.

---

## 🎯 Main Features

### 🛍️ Product Marketplace

Buyers can browse products listed by rural producers.

Products include:

- Organic Rice
- Wheat
- Cotton Saree
- Fresh Vegetables
- Raw Honey
- Handicraft Items

Each product can display its:

- Name
- Price
- Unit
- Available stock
- Producer
- Location
- Category
- Description

### 👤 Buyer Account

Buyers can:

- Create an account
- Login
- Browse products
- Search and filter products
- Add products to cart
- Place bulk orders
- View order information
- Track orders

### 🌾 Producer Account

Producers can:

- Create an account
- Login
- List new products
- Manage their products
- View buyer orders
- Check sales information
- Create auctions for their products

### 🛒 Shopping Cart

The cart allows buyers to:

- Add products
- Change quantities
- Remove products
- View subtotal
- Place bulk orders

### 📦 Order Management

After placing an order, the system provides order information and a basic order-tracking flow.

The tracking stages include:

**Order Placed → Confirmed → Packed → Shipped → Delivered**

### 🔨 Auction & Bidding System

RuralConnect also includes an auction feature.

Producers can:

- Create an auction
- Select a product
- Set a starting bid
- Set the quantity
- Select an auction duration

Buyers can:

- View live auctions
- Place bids
- See the current highest bid
- View bid history
- See the winning bidder after the auction ends

### 🤖 RuralConnect Helper

The project includes a simple rule-based **RuralConnect Helper** that can answer basic questions about the marketplace, auctions, and bidding.

This is a demonstration feature and does not use a real AI/LLM service.

---

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Java, Java Servlets, Jakarta Servlet API, Apache Tomcat 11 |
| Database | MySQL, JDBC, SQL |
| Development Tools | Visual Studio Code, Apache Maven, Git, Chrome |

---

## 🏗️ System Architecture

```text
Frontend
HTML + CSS + JavaScript
        ↓
Apache Tomcat
        ↓
Java Servlets
        ↓
JDBC
        ↓
MySQL Database
```

The frontend sends requests to Java Servlets running on Apache Tomcat.

The Servlets communicate with the MySQL database using JDBC.

---

## 📂 Project Structure

```text
RuralConnect/
│
├── assets/
│
├── backend/
│   └── Java/Tomcat backend files
│
├── css/
│   └── style.css
│
├── js/
│   ├── app.js
│   └── ai-demo.js
│
├── database.sql
├── index.html
├── RuralConnect.html
├── README.md
└── .gitignore
```

---

## 🗄️ Database

The project uses MySQL for storing application data.

The database can contain information related to:

- Users
- Products
- Orders
- Auctions
- Bids

The `database.sql` file contains the database setup used by the project.

---

## 🔄 How RuralConnect Works

### Producer Flow

```text
Producer Login
      ↓
Producer Dashboard
      ↓
Add Product
      ↓
Product Listed
      ↓
Buyer Places Order / Participates in Auction
      ↓
Producer Manages Order or Auction
```

### Buyer Flow

```text
Buyer Login
      ↓
Browse Marketplace
      ↓
Select Product
      ↓
Add to Cart
      ↓
Place Bulk Order
      ↓
Track Order
```

### Auction Flow

```text
Producer Creates Auction
          ↓
Buyer Views Auction
          ↓
Buyer Places Bid
          ↓
Other Buyers Can Bid
          ↓
Auction Ends
          ↓
Highest Bidder Wins
```

---

## ⭐ Advantages of the Project

- Provides a digital marketplace for rural producers.
- Helps buyers discover products from different regions.
- Supports bulk ordering.
- Includes producer and buyer dashboards.
- Demonstrates order tracking.
- Includes an auction and bidding system.
- Demonstrates Java Servlet and MySQL integration.
- Provides practical experience with client-server architecture.
- Can be extended into a larger e-commerce and supply-chain platform.

---

## 📚 Learning Outcomes

Through this project, we learned:

- Java programming
- Java Servlets
- Apache Tomcat
- JDBC
- MySQL
- SQL
- HTML, CSS, and JavaScript
- Client-server architecture
- Database connectivity
- CRUD concepts
- Web application development
- Git
- Team-based project development

---

## 💡 Purpose of the Project

RuralConnect demonstrates how a digital platform can connect rural producers and buyers.

The project combines a marketplace with ordering, tracking, and auction functionality to create a practical example of a rural e-commerce and supply-chain application.

---

## 🚀 Future Scope

The project can be extended by adding:

- Online payment integration
- Real-time notifications
- Advanced order tracking
- Product reviews and ratings
- Product image uploads
- Advanced search and filtering
- Real-time auction updates
- Mobile application support
- Cloud deployment
- Improved authentication and security
- Additional database and reporting features

---

## 📖 Project Message

**Connect → Trade → Bid → Grow**

RuralConnect demonstrates how Java and web technologies can be combined to create a practical marketplace platform connecting rural producers with buyers.

---

## 🙏 Acknowledgement

We would like to thank our faculty for giving us the opportunity to develop RuralConnect and apply concepts of Java, web development, database management, and software development in a practical project.

---

## 📜 License

This project is created for educational and academic purposes.
