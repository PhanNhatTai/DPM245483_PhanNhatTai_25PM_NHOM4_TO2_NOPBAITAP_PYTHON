#Giải thích kết quả tính toán của các biểu thức
"""
Yêu cầu :
Cho các biến với giá trị : 
i1 = 2 
i2 = 5 
i3 = -3 
d1 = 2.0 
d2 = 5.0 
d3 = -0.5
Cho biết kết quả và giải thích cách thực hiện của các lệnh sau:
(a) i1 + (i2 * i3) = -13 Cách thực hiện : đầu tiên chương trình sẽ nhân i2 và i3 sau đó cộng với i1
(b) i1 * (i2 + i3) = 4 Cách thực hiện : đầu tiên chương trình sẽ cộng i2 và i3 (chương trình ưu tiên thực hiện theo thứ tự trong ngoặc -> nhân -> chia -> cộng -> trừ) sau đó nhân với i1
(c) i1 / (i2 + i3) = 1 Cách thực hiện : đầu tiên chương trình sẽ cộng i2 và i3 (chương trình ưu tiên thực hiện theo thứ tự trong ngoặc -> nhân -> chia -> cộng -> trừ) sau đó chia với i1
(d) i1 // (i2 + i3) = 1 Cách thực hiện : đầu tiên chương trình sẽ cộng i2 và i3 (chương trình ưu tiên thực hiện theo thứ tự trong ngoặc -> nhân -> chia -> cộng -> trừ) sau đó chia với i1 (chỉ lấy phần nguyên bỏ phần thập phân)
(e) i1 / i2 + i3 = -2.6 Cách thực hiện : đầu tiên chương trình sẽ chia i1 và i2 sau đó cộng với i3
(f) i1 // i2 + i3 =-3 Cách thực hiện : đầu tiên chương trình sẽ chia i1 và i2 (do dùng phép toán // nên sẽ làm tròn kết quả) sau đó cộng cho i3
(g) 3 + 4 + 5 / 3 =8.666666666666666 Cách thực hiện :đầu tiên chương trình sẽ thực hiện phép toán 5/3 sau đó sẽ thực hiện phép toán 3+4 rồi cộng 2 kết quả vừa có với nhau
(h) 3 + 4 + 5 // 3 = 8 Cách thực hiện :đầu tiên chương trình sẽ thực hiện phép toán 5/3 (làm tròn) sau đó sẽ thực hiện phép toán 3+4 rồi cộng 2 kết quả vừa có với nhau
(i) (3 + 4 + 5) / 3 =4 Cách thực hiện :đầu tiên chương trình sẽ thực hiện các phép tính trong ngoặc sau đó lấy kết quả đó chia cho 3
(j) (3 + 4 + 5) // 3 =4 Cách thực hiện :đầu tiên chương trình sẽ thực hiện các phép tính trong ngoặc sau đó lấy kết quả đó chia cho 3
(k) d1 + (d2 * d3) =-0.5 Cách thực hiện :đầu tiên chương trình sẽ thực hiện phép toán d2*d3 (do nằm trong ngoặc nên thực hiện trước)rồi dùng kết quả đó cộng cho d1
(l) d1 + d2 * d3=-0.5 Cách thực hiện :đầu tiên chương trình sẽ thực hiện phép toán d2*d3 (do là phép nhân nên thực hiện trước) rồi dùng kết quả đó cộng cho d1
(m) d1 / d2 - d3 =0.9 Cách thực hiện :đầu tiên chương trình sẽ thực hiện phép toán d1/d2 (do là phép chia nên thực hiện trước) rồi dùng kết quả đó trừ cho d3
(n) d1 / (d2 - d3) =0.36363636363636365 Cách thực hiện:đầu tiên chương trình sẽ thực hiện phép toán d2-d3 (do nằm trong ngoặc nên thực hiện trước) rồi dùng kết quả đó chia cho d1
(o) d1 + d2 + d3 / 3 =6.833333333333333 Cách thực hiện: đầu tiên chương trình sẽ thực hiện phép toán d3/3 (do phép chia nên thức hiện trước) sau đó sẽ dùng kết quả cộng với d1 và d2
(p) (d1 + d2 + d3) / 3 =2.1666666666666665 Cách thực hiện: đầu tiên chương trình sẽ thực hiện các phép tính d1+d2+d3 (do nằm trong ngoặc nên sẽ thực hiện trước) rồi dùng kết quả đó chia cho 3
(q) d1 + d2 + (d3 / 3) =6.833333333333333 Cách thực hiện: đầu tiên chương trình sẽ thực hiện phép toán d3/3 (do nằm trong ngoặc nên thức hiện trước) sau đó sẽ dùng kết quả cộng với d1 và d2
(r) 3 * (d1 + d2) * (d1 - d3) =52.5 Cách thực hiện : đầu tiên chương trình sẽ thức hiện phép tính d1+d2(do nằm trong ngoặc nên thức hiện trước) sau đó chương trình sẽ thức hiện phép tính d1-d3(do nằm trong ngoặc nên thực hiện trước) rối sau đó ta sẽ nhân 3 với kết quả của 2 phép tính ta vừa thực hiện
"""