import random


def check_guess(secret, guess):
    """比较玩家的猜测和答案，返回 "high"、"low" 或 "correct"。"""
    if guess > secret:
        return "high"
    elif guess < secret:
        return "low"
    else:
        return "correct"


def main():
    # 随机生成 1 到 100 之间的整数作为答案
    secret = random.randint(1, 100)
    attempts = 0  # 记录有效猜测次数

    print("欢迎来到猜数字游戏！我已经想好了一个 1 到 100 之间的数字。")

    while True:
        raw = input("请输入你的猜测：")

        # 检查输入是否为有效整数
        try:
            guess = int(raw)
        except ValueError:
            print("请输入有效数字")
            continue

        attempts += 1
        result = check_guess(secret, guess)

        if result == "high":
            print("太大了")
        elif result == "low":
            print("太小了")
        else:
            print(f"恭喜！你用了 {attempts} 次猜中")
            break


if __name__ == "__main__":
    main()
