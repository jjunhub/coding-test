start_hour, start_min, start_sec = map(int, input().split(":"))
end_hour, end_min, end_sec = map(int, input().split(":"))

start_time = start_hour * 60 * 60 + start_min * 60 + start_sec 
end_time = end_hour * 60 * 60 + end_min * 60 + end_sec 

if start_time > end_time :
  end_time += 24 * 60 * 60

remain_time = end_time - start_time
remain_hour = remain_time // ( 60 * 60)
remain_time = remain_time % (60*60)
remain_min = remain_time // 60
remain_sec = remain_time % 60

print("%02d:%02d:%02d" %(remain_hour, remain_min, remain_sec))