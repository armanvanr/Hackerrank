def sockMerchant(n, ar):
    unique = list(set(ar))
    sum = 0
    for col in unique:
        sum += (ar.count(col))//2
    return sum


sock_list=[1,2,1,2,1,3,2]
print(sockMerchant(len(sock_list),sock_list))