total_secs = int(input("How many seconds? "))
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60
print("This translates to", hours, "hours", minutes, "minutes and" , secs_finally_remaining , "seconds")