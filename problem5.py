
# Rearrange array by interchanging positions of even and odd elements in the given array

arr = list(map(int,input().split()))
n = len(arr)


for i in range(n):
	if arr[i]%2 == 0 and arr[i+1]%2 != 0:
		temp = arr[]
