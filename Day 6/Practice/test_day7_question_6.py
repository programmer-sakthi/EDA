import sqlite3
import pandas as pd

# Step 1: Connect to in-memory SQLite database
conn = sqlite3.connect(":memory:")  # use glamnest_db.db instead for file-based

cursor = conn.cursor()

# Step 2: Create appointments table
cursor.execute(
    """
CREATE TABLE appointments (
    appointment_id VARCHAR(20),
    user_id VARCHAR(20),
    user_name VARCHAR(100),
    gender VARCHAR(10),
    area VARCHAR(50),
    city VARCHAR(50),
    service_id VARCHAR(20),
    provider_id VARCHAR(20),
    appointment_date DATE,
    appointment_time TIME,
    status VARCHAR(20),
    payment_id VARCHAR(20),
    amount DECIMAL(10,2),
    discount_percent DECIMAL(5,2),
    tax DECIMAL(5,2),
    discounted_amount DECIMAL(10,2),
    tax_amount DECIMAL(10,2),
    final_amount DECIMAL(10,2),
    payment_method VARCHAR(50),
    service_rating DECIMAL(3,1),
    service_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    provider_name VARCHAR(100),
    specialization VARCHAR(50),
    provider_rating DECIMAL(3,1)
)
"""
)

# Step 3: Insert sample record
cursor.execute(
    """
INSERT INTO appointments (
    appointment_id, user_id, user_name, gender, area, city,
    service_id, provider_id, appointment_date, appointment_time,
    status, payment_id, amount, discount_percent, tax,
    discounted_amount, tax_amount, final_amount, payment_method,
    service_rating, service_name, category, price, provider_name,
    specialization, provider_rating
) VALUES 
('APT0001', 'USR001', 'Aisha Khan', 'Female', 'Andheri West', 'Mumbai',
 'SRV101', 'PRV501', '2024-08-20', '14:30:00', 'Completed', 'PMT001', 1500.00, 10.00, 5.00,
 1350.00, 67.50, 1417.50, 'UPI', 4.5, 'Hair Spa', 'Hair Care', 1500.00, 'Riya Sharma', 'Hair Stylist', 4.8),

('APT0002', 'USR002', 'Rohan Mehta', 'Male', 'Koramangala', 'Bangalore',
 'SRV102', 'PRV502', '2024-08-21', '16:00:00', 'Completed', 'PMT002', 1200.00, 15.00, 5.00,
 1020.00, 51.00, 1071.00, 'Credit Card', 4.2, 'Facial Clean-up', 'Skin Care', 1200.00, 'Meena Rao', 'Dermatologist', 4.7),

('APT0003', 'USR003', 'Sneha Patel', 'Female', 'Banjara Hills', 'Hyderabad',
 'SRV103', 'PRV503', '2024-08-22', '11:00:00', 'Cancelled', 'PMT003', 1800.00, 0.00, 0.00,
 1800.00, 0.00, 1800.00, 'Cash', NULL, 'Hair Cut', 'Hair Care', 1800.00, 'Sunil Verma', 'Hair Stylist', 4.5),

('APT0004', 'USR004', 'Vikram Joshi', 'Male', 'Salt Lake', 'Kolkata',
 'SRV104', 'PRV504', '2024-08-23', '10:30:00', 'Completed', 'PMT004', 2500.00, 20.00, 5.00,
 2000.00, 100.00, 2100.00, 'Debit Card', 4.9, 'Body Massage', 'Wellness', 2500.00, 'Arjun Roy', 'Massage Therapist', 4.9),

('APT0005', 'USR005', 'Neha Gupta', 'Female', 'Viman Nagar', 'Pune',
 'SRV105', 'PRV505', '2024-08-24', '13:15:00', 'Completed', 'PMT005', 900.00, 5.00, 5.00,
 855.00, 42.75, 897.75, 'UPI', 4.4, 'Pedicure', 'Nail Care', 900.00, 'Sara Khan', 'Nail Technician', 4.6),

('APT0006', 'USR006', 'Amit Sharma', 'Male', 'Gachibowli', 'Hyderabad',
 'SRV106', 'PRV506', '2024-08-25', '15:45:00', 'Completed', 'PMT006', 2000.00, 10.00, 5.00,
 1800.00, 90.00, 1890.00, 'Net Banking', 4.3, 'Hair Color', 'Hair Care', 2000.00, 'Sandeep Kaur', 'Hair Stylist', 4.7),

('APT0007', 'USR007', 'Priya Iyer', 'Female', 'Powai', 'Mumbai',
 'SRV107', 'PRV507', '2024-08-26', '12:00:00', 'No Show', 'PMT007', 1600.00, 0.00, 0.00,
 1600.00, 0.00, 1600.00, 'Cash', NULL, 'Waxing', 'Body Care', 1600.00, 'Alka Desai', 'Beautician', 4.4),

('APT0008', 'USR008', 'Karan Malhotra', 'Male', 'Anna Nagar', 'Chennai',
 'SRV108', 'PRV508', '2024-08-27', '17:30:00', 'Completed', 'PMT008', 2200.00, 10.00, 5.00,
 1980.00, 99.00, 2079.00, 'Credit Card', 4.6, 'Beard Trim', 'Grooming', 2200.00, 'Vikash Singh', 'Barber', 4.8),

('APT0009', 'USR009', 'Divya Reddy', 'Female', 'BTM Layout', 'Bangalore',
 'SRV109', 'PRV509', '2024-08-28', '09:00:00', 'Completed', 'PMT009', 1400.00, 5.00, 5.00,
 1330.00, 66.50, 1396.50, 'UPI', 4.7, 'Manicure', 'Nail Care', 1400.00, 'Radha Menon', 'Nail Technician', 4.5),

('APT0010', 'USR010', 'Ravi Deshmukh', 'Male', 'Jayanagar', 'Bangalore',
 'SRV110', 'PRV510', '2024-08-29', '18:00:00', 'Completed', 'PMT010', 3000.00, 15.00, 5.00,
 2550.00, 127.50, 2677.50, 'Debit Card', 4.9, 'Full Body Spa', 'Wellness', 3000.00, 'Kiran Bedi', 'Massage Therapist', 5.0)
"""
)

conn.commit()

# Step 4: Query the data
df = pd.read_sql_query("SELECT * FROM appointments", conn)
print(df)

conn.close()
