# --- Checkpoint Assingment 01: ---
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
# -- Acquire user age --
user_age = int(input('What is your age? '))
# -- calculate max heert rate --
max_heart_rate = 220 - user_age
# -- Calculate range of heart rate --
min_heart_rate_range = int(max_heart_rate * 0.65) # - slowest rate / start of range -
max_heart_rate_range = int(max_heart_rate * 0.85) # - Fastest rate / end of range -
print (f'When exercising to strengthen your heart, you should keep your heart rate between {min_heart_rate_range} & {max_heart_rate_range} b.p.m.')

