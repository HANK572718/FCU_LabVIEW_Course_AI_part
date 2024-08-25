
def test_tensor_operations():
    import platform
    import sys
    import torch
    import time
    results = []  # 用於存儲所有結果的列表

    # 1. 顯示 Python 版本資訊、位元數、位置
    python_version = platform.python_version()
    python_bits = platform.architecture()[0]
    python_executable = sys.executable  # 取得 Python 執行檔位置

    results.append("=== Python Information ===")
    results.append(f"Version: {python_version}")
    results.append(f"Bits: {python_bits}")
    results.append(f"Executable Location: {python_executable}\n")

    # 2. 顯示可用的 Torch devices
    devices = [torch.device(
        'cpu')] + [torch.device(f'cuda:{i}') for i in range(torch.cuda.device_count())]

    results.append("=== Torch Devices ===")
    torch_vision = torch.__version__
    results.append(f"Torch Version: {torch_vision}")
    for device in devices:
        results.append(str(device))

    # 3. 測試每個設備的運行時間，以及進行複雜的 Tensor 操作
    tensor_size = (1000, 1000)  # 調整 tensor 矩陣的大小
    repetitions = 1  # 重複運行的次數
    results.append("\n=== Tensor Computation Time ===")
    for device in devices:
        start_time = time.time()

        # 創建隨機 tensor
        tensor_a = torch.randn(tensor_size, device=device)
        tensor_b = torch.randn(tensor_size, device=device)

        # 進行多次操作以增加總耗時
        for _ in range(repetitions):
            tensor_sum = tensor_a + tensor_b  # Tensor 加法
            tensor_product = tensor_a @ tensor_b  # 矩陣乘法
            tensor_mean = tensor_sum.mean()  # 計算平均值

        elapsed_time = time.time() - start_time
        results.append(
            f"Time taken for tensor operations on {device}: {elapsed_time:.4f} seconds")

    # 4. 驗證 OpenVINO 安裝以及可用設備
    try:
        from openvino.runtime import Core  # 更新引用來匹配 openvino 的最近版本
        ie = Core()
        available_devices = ie.available_devices
        results.append("\n=== OpenVINO Information ===")
        results.append("OpenVINO is installed.")
        results.append("Available devices: " + str(available_devices))
    except ImportError:
        results.append("\n=== OpenVINO Information ===")
        results.append("OpenVINO is NOT installed.")

    # 將結果轉換為字串並返回
    return "\n".join(results)

def get_info():
    import platform
    import sys
    import time
    results = []  # 用於存儲所有結果的列表

    # 1. 顯示 Python 版本資訊、位元數、位置
    python_version = platform.python_version()
    python_bits = platform.architecture()[0]
    python_executable = sys.executable  # 取得 Python 執行檔位置

    results.append("=== Python Information ===")
    results.append(f"Version: {python_version}")
    results.append(f"Bits: {python_bits}")
    results.append(f"Executable Location: {python_executable}\n")
    return "\n".join(results)

# 調用測試函數並打印結果
if __name__ == "__main__":
    output = test_tensor_operations()
    # output = get_info()
    print(output)
