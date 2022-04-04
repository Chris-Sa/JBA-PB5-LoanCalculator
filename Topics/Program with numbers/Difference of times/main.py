# put your python code here

start_hour = int(input())
start_min = int(input())
start_sec = int(input())

end_hour = int(input())
end_min = int(input())
end_sec = int(input())

elapsed_hour = end_hour - start_hour
elapsed_min = end_min - start_min
elapsed_sec = end_sec - start_sec

seconds_hour = 3600
elapsed_hour *= seconds_hour
elapsed_min *= 60

elapsed_sec += elapsed_hour
elapsed_sec += elapsed_min

print(elapsed_sec)
