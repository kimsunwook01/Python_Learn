# 상품 가격, 부가세, 배송료 합하여 출력하기

price = int(input("상품의 가격: ")) #상품가격
num = int(input("상품의 개수: "))   #상품개수
surtax = price * num * 0.1       #부가세
delivery = 3000 #배송료
allprice = price * num + surtax + delivery #가격 합계

# 결과출력
print("부가세(%): 10%")
print(f"배송료: {delivery}")
print(f"전체가격: {allprice:.0f}")
