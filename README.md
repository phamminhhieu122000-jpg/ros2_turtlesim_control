


# ROS 2 Humble - Turtlesim Keyboard Teleop Control (WASD)

Project này chứa một package ROS 2 viết bằng Python (`turtlesim_control`) cho phép người dùng điều khiển chú rùa trong `turtlesim` di chuyển thời gian thực bằng các phím điều hướng trực quan **W-A-S-D** thay vì sử dụng các phím mũi tên mặc định.

## 🚀 Các tính năng chính
- **Điều khiển trực quan:** Sử dụng cụm phím phổ biến `W` (Tiến), `S` (Lùi), `A` (Xoay trái), `D` (Xoay phải).
- **Phanh khẩn cấp:** Bấm `SPACE` (Khoảng trắng) để triệt tiêu vận tốc, giúp rùa dừng lại ngay lập tức.
- **Thời gian thực:** Đọc trực tiếp sự kiện phím bấm từ Terminal mà không cần nhấn `Enter`.

---

## 🛠️ Yêu cầu hệ thống (Prerequisites)
- **Hệ điều hành:** Ubuntu 22.04 LTS
- **Môi trường:** ROS 2 Humble Core / Desktop (Hoặc chạy qua Docker Container)
- **Package phụ thuộc:** `rclpy`, `geometry_msgs`, `turtlesim`

---

## 📦 Hướng dẫn cài đặt và Biên dịch

Tạo thư mục dự án mới
# Tạo thư mục dự án mới (nếu chưa có)
mkdir -p ~/Study/ROS2/workspace/src
1. **Di chuyển vào thư mục nguồn của Workspace:**
   ```bash
   cd ~/workspace/src

```

2. **Clone mã nguồn dự án (Nếu tải từ GitHub về máy mới):**
```bash
git clone [https://github.com/phamminhhieu122000-jpg/ros2_turtlesim_control.git](https://github.com/phamminhhieu122000-jpg/ros2_turtlesim_control.git) turtlesim_control

```


3. **Quay về thư mục gốc và biên dịch sạch:**
```bash
cd ~/workspace
rm -rf build/ install/ log/
colcon build --packages-select turtlesim_control

```


4. **Nạp môi trường:**
```bash
source install/setup.bash

```



---

## 🎮 Hướng dẫn Chạy & Điều khiển

Để khởi chạy dự án, bạn cần mở **3 cửa sổ Terminal** độc lập (Nếu dùng Docker, hãy chắc chắn đã chạy `xhost +local:docker` ngoài máy thật để mở cổng đồ họa).

### Terminal 1: Bật màn hình mô phỏng con rùa

```bash
ros2 run turtlesim turtlesim_node

```

### Terminal 2: Khởi động bộ điều khiển bàn phím WASD

```bash
cd ~/workspace
source install/setup.bash
ros2 run turtlesim_control wasd_teleop

```

### Terminal 3: (Tùy chọn) Kiểm tra luồng dữ liệu Topic

```bash
ros2 topic echo /turtle1/cmd_vel

```

---

## 🗺️ Sơ đồ sơ lược hệ thống (Cấu trúc Node & Topic)

* **Node phát (Publisher):** `/wasd_control_node`
* **Node nhận (Subscriber):** `/turtlesim`
* **Topic truyền tải:** `/turtle1/cmd_vel` [kiểu dữ liệu: `geometry_msgs/msg/Twist`]

```
[Bàn phím] -> [/wasd_control_node] --(/turtle1/cmd_vel)--> [/turtlesim (Hiển thị đồ họa)]

```

---
