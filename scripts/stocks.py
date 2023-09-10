#import yfinance as yf

#ticker = yf.Ticker('FLRY3.SA')
#df = ticker.history(period='120d')
#print(df)

def solution(sequence):
    if sequence[0] == '(':
        sequence[-1] == ')'
        
            
    if sequence[0] == '[':
        sequence[-1] == ']'
            
    if sequence[0] == '{':
        sequence[-1] == '}'

def solution(a, b):
    a_list = list(a)
    b_list = list(b)
    
    count_a = {}
    count_b = {}
    
    for i in a_list:
        count = a_list.count(i)
        count_a[i] = count
    print(count_a)

    for i in b_list:
        count = b_list.count(i)
        count_b[i] = count
    print(count_b)

    new_dict = {}
    for i in count_a:
        if count_a[i] < count_b[i]:
            new_dict[i] = count_b[i]
        else:
            new_dict[i] = 0

    print(min(new_dict.values()))
    

# def solution(p):
    list = []
    for i, j in p:
        distance = ( ( p[i[0]] - p[j[0]] ) ** 2 + ( p[i[1]] - p[j[1]] ) ** 2 ) ** 0.5
        list.append(distance)
    
    print(min(list))

test = solution([[0, 11], [-7, 1], [-5, -3]])
print(test[0])


