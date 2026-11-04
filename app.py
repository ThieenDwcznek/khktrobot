import streamlit as st
import pandas as pd
import datetime

# 1. Cấu hình giao diện trang web
st.set_page_config(
    page_title="Robot Chăm Sóc Cây Trồng - KHKT",
    page_icon="🌱",
    layout="wide"
)

# 2. Tiêu đề dự án
st.title("🌱 HỆ THỐNG GIÁM SÁT & ĐIỀU KHIỂN ROBOT CHĂM SÓC CÂY")
st.caption("Dự án Khoa học Kỹ thuật | Tác giả: Trương Thiên Đức & Lê Trần Hà My - THPT Trần Quốc Tuấn")

st.divider()

# 3. Khối thông số cảm biến môi trường
st.header("📊 Thông số cảm biến thực tế")

col1, col2, col3, col4 = st.columns(4)

# Giả lập giá trị độ ẩm đất
do_am_dat = 28  # Giả định 28%

with col1:
    if do_am_dat < 30:
        st.metric(
            label="Độ ẩm đất", 
            value=f"{do_am_dat} %", 
            delta="-2% (Đất khô - Ẩm <30%)", 
            delta_color="inverse"
        )
    else:
        st.metric(label="Độ ẩm đất", value=f"{do_am_dat} %", delta="Bình thường")

with col2:
    st.metric(label="Nhiệt độ không khí", value="31 °C", delta="+1°C")

with col3:
    st.metric(label="Độ ẩm không khí", value="65 %")

with col4:
    st.metric(label="Nguồn Pin Mặt Trời", value="85 %", delta="Đang nạp")

# Cảnh báo tự động nếu đất khô
if do_am_dat < 30:
    st.warning("⚠️ **CẢNH BÁO TỰ ĐỘNG:** Độ ẩm đất rơi xuống dưới ngưỡng 30%. Robot chuẩn bị tự động kích hoạt Bơm 1 tưới nước!")

st.divider()

# 4. Bảng điều khiển các máy bơm (3 Bơm)
st.header("🎮 Bảng điều khiển thiết bị chấp hành")
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("💦 Kích hoạt Bơm 1 (Tưới nước gốc)", use_container_width=True):
        st.success("✅ [LỆNH ĐÃ GỬI]: Đã bật Bơm 1 xịt tưới gốc cây!")

with c2:
    if st.button("🌿 Kích hoạt Bơm 2 (Bón phân lỏng)", use_container_width=True):
        st.info("✅ [LỆNH ĐÃ GỬI]: Đã bật Bơm 2 phân phối dinh dưỡng!")

with c3:
    if st.button("💨 Kích hoạt Bơm 3 (Phun thuốc sương)", use_container_width=True):
        st.warning("✅ [LỆNH ĐÃ GỬI]: Đã bật Bơm 3 phun dung dịch xử lý bệnh dạng sương!")

st.divider()

# 5. Khối xử lý hình ảnh AI & ESP32-CAM
st.header("📸 Nhận diện bệnh trên lá bằng AI (Server Python)")
col_img, col_info = st.columns([1, 1])

with col_img:
    st.subheader("Hình ảnh từ Camera ESP32-CAM")
    # Khung hiển thị ảnh mẫu
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Leaf_spot.jpg/640px-Leaf_spot.jpg", 
        caption="Ảnh lá cây chụp thực tế bởi ESP32-CAM",
        use_column_width=True
    )

with col_info:
    st.subheader("Kết quả chẩn đoán từ Server AI")
    st.error("⚠️ **Chẩn đoán:** Phát hiện đốm nấm lá (Leaf Spot) trên bề mặt lá.")
    st.write("**Khuyến nghị:** Kích hoạt Bơm 3 để phun dung dịch xử lý dạng sương trong 3 giây.")
    
    if st.button("🎯 Xử lý ngay (Tự động phun dung dịch)"):
        st.success("🤖 Robot đang di chuyển đến vị trí và kích hoạt Bơm 3!")

st.divider()

# 6. Nhật ký lưu trữ lịch sử
st.header("📜 Nhật ký hoạt động hệ thống")
df = pd.DataFrame({
    "Thời gian": ["08:00:12", "09:30:45", "10:15:00"],
    "Độ ẩm đất": ["35%", "29%", "28%"],
    "Sự kiện / Lệnh": ["Kiểm tra định kỳ", "Tự động bật Bơm 1 (Tưới nước)", "ESP32-CAM chụp ảnh & AI phát hiện bệnh"],
    "Trạng thái": ["Hoạt động tốt", "Hoàn tất tưới", "Đã ghi nhận"]
})
st.dataframe(df, use_container_width=True)
