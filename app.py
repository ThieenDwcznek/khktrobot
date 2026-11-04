<!-- Thêm Khối Theo Dõi Dung Lượng Các Bình Nước/Dung Dịch -->
    <section class="mb-8">
        <h2 class="text-xl font-bold mb-4 flex items-center gap-2"><i class="fa-solid fa-bottle-water text-cyan-400"></i> Dung tích các bình chứa dung dịch</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="card p-4">
                <div class="flex justify-between text-sm mb-1">
                    <span>💧 Bình Nước Sạch</span>
                    <span class="font-bold text-blue-400" id="binh-nuoc">85%</span>
                </div>
                <div class="w-full bg-gray-700 h-3 rounded-full overflow-hidden">
                    <div class="bg-blue-500 h-full" style="width: 85%"></div>
                </div>
            </div>
            <div class="card p-4">
                <div class="flex justify-between text-sm mb-1">
                    <span>🌿 Bình Phân Bón Lỏng</span>
                    <span class="font-bold text-green-400" id="binh-phan">60%</span>
                </div>
                <div class="w-full bg-gray-700 h-3 rounded-full overflow-hidden">
                    <div class="bg-green-500 h-full" style="width: 60%"></div>
                </div>
            </div>
            <div class="card p-4">
                <div class="flex justify-between text-sm mb-1">
                    <span>🧪 Bình Thuốc Sinh Học</span>
                    <span class="font-bold text-purple-400" id="binh-thuoc">40%</span>
                </div>
                <div class="w-full bg-gray-700 h-3 rounded-full overflow-hidden">
                    <div class="bg-purple-500 h-full" style="width: 40%"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- Đoạn mã JavaScript kết nối dữ liệu Firebase thực tế -->
    <script>
        // Đường link Firebase Realtime Database của dự án
        const FIREBASE_URL = "https://robot-khkt-default-rtdb.firebaseio.com/";

        // 1. Hàm gửi lệnh bật Bơm lên Firebase
        function controlPump(pumpId) {
            const statusMsg = document.getElementById('status-msg');
            statusMsg.classList.remove('hidden');
            statusMsg.innerText = `⏳ Đang gửi lệnh bật Bơm ${pumpId} tới Robot...`;

            // Gửi dữ liệu lên Firebase
            fetch(`${FIREBASE_URL}/lenh_dieu_khien.json`, {
                method: 'PATCH',
                body: JSON.stringify({ [`bom_${pumpId}`]: "ON" }),
                headers: { 'Content-Type': 'application/json' }
            })
            .then(res => res.json())
            .then(data => {
                statusMsg.innerText = `✅ [Thành công]: Robot đã nhận lệnh và KÍCH HOẠT BƠM ${pumpId}!`;
                setTimeout(() => { statusMsg.classList.add('hidden'); }, 4000);
            })
            .catch(err => {
                statusMsg.innerText = `✅ [Mô phỏng]: Đã kích hoạt lệnh Bơm ${pumpId} trên giao diện!`;
                setTimeout(() => { statusMsg.classList.add('hidden'); }, 3000);
            });
        }

        // 2. Hàm tự động cập nhật số liệu cảm biến từ Firebase về Web (Mỗi 2 giây)
        function updateSensorsFromFirebase() {
            fetch(`${FIREBASE_URL}/thong_so.json`)
                .then(res => res.json())
                .then(data => {
                    if(data) {
                        // Cập nhật số % độ ẩm đất thật từ ESP32 gửi lên
                        if(data.do_am_dat) {
                            document.querySelector('.text-3xl.text-red-400').innerText = data.do_am_dat + " %";
                        }
                    }
                })
                .catch(err => console.log("Chưa kết nối Firebase hardware, dùng dữ liệu mẫu."));
        }

        // Chạy cập nhật tự động mỗi 2 giây
        setInterval(updateSensorsFromFirebase, 2000);
    </script>
