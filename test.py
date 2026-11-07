total_amount = float(input("Tổng tiền: "))
member_type = input("Loại thành viên (VIP/Gold/Normal): ").lower()

if member_type != "vip":
    is_holiday = input("Ngày hội mua sắm (Flash sale) yes/no? ").strip().lower()
else: pass

if member_type == "vip":
    vip = f"Giảm 30%, tổng là {int(total_amount * 0.7)}" if total_amount >= 2_000_000 else f"Giảm 20%, tổng là {int(total_amount * 0.8)}"
    print(vip)
elif member_type == "gold":
    gold = f"Giảm 15%, tổng là {int(total_amount * 0.85)}" if total_amount >= 1_000_000 or is_holiday == "yes" else f"Giảm 10%, tổng là {int(total_amount * 0.9)}"
    print(gold)

elif member_type == "normal" and (total_amount >= 3_000_000 or is_holiday == "yes"):
    print(f"Giảm 5%, tổng là {int(total_amount * 0.95)}")
else:
    print("Không được giảm giá:(")