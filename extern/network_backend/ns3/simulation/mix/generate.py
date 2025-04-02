# 打开一个输出文件，准备写入数据
with open('output.txt', 'w') as f:
    # 生成前64行，a=128, b从0到63
    for b in range(0, 64):
        a = 128
        c = 100
        d = 0.0005
        f.write(f"{a} {b} {c}Gbps {d}ms 0\n")

    # 生成后64行，a=129, b从64到127
    for b in range(64, 128):
        a = 129
        c = 100
        d = 0.0005
        f.write(f"{a} {b} {c}Gbps {d}ms 0\n")

print("文件生成完毕，已保存为 'output.txt'.")

