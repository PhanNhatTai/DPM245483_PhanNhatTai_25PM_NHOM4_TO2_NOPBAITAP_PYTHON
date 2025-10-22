"""
Kiểm tra kết quả thực hiện 
Cho 3 hàm dưới đây: 
def sum1(n): 
    s = 0 
    while n > 0: 
        s += 1 1 2 3 4 5
        n -= 1 4 3 2 1 0
    return s 
def sum2(): 
    global val 
    s = 0 
    while val > 0: 
        s += 1 
        val -= 1 
    return s 
def sum3(): 
    s = 0 
    for i in range(val, 0, -1): 
        s += 1 
    return s
Hãy cho biết kết quả sau khi gọi các lệnh dưới đây:
Trường hợp 1:
def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum2()) 
    print(sum3()) 
main()
Kết quả in ra là : 5,5,0
def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum3()) 
    print(sum2()) 
main() 
Kết quả in ra là : 5,5,5
def main(): 
    global val 
    val = 5 
    print(sum2()) 
    print(sum1(5)) 
    print(sum3()) 
main()
Kết quả in ra là : 5,5,0
"""