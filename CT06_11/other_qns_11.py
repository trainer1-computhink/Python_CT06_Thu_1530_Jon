# =========================================
# TASK 13: Scholarship Eligibility System
# =========================================
 
# A student may receive a scholarship.
 
# The student must not be banned.
 
# After that, the student qualifies if they scored at least 85 and
# attended at least 90 percent of classes, or if they scored at least
# 70 and have won a competition.
 
# Otherwise → "Not Eligible"
 
# 1. Ask for:
#    - score
#    - attendance
#    - won_competition (yes/no)
#    - banned (yes/no)
 
 
# -----------------------------------------
 
# =========================================
# TASK 14: Smart Home Security System
# =========================================
 
# A home alarm system decides whether to trigger an alarm.
 
# The alarm should trigger if the door is open while the owner is not
# at home, or if a window is open during the night, or if motion is
# detected while pet mode is off.
 
# Otherwise → "All Safe"
 
# 1. Ask for:
#    - door_open (yes/no)
#    - owner_home (yes/no)
#    - window_open (yes/no)
#    - time ("day"/"night")
#    - motion_detected (yes/no)
#    - pet_mode (yes/no)
 
 
# -----------------------------------------
 
# =========================================
# TASK 15: Exam Pass System
# =========================================
 
# A student can pass an exam in different ways.
 
# A student passes if they scored at least 50 in both math and science,
# or if their overall average is at least 60 and they did not cheat.
 
# However, if the student cheated, they will fail regardless of their scores.
 
# 1. Ask for:
#    - math marks
#    - science marks
#    - overall average
#    - cheating (yes/no)
 
 
# -----------------------------------------
 
# =========================================
# TASK 16: Input Logic Filter
# =========================================
 
data = ["10", "abc", "5", "20", "-3", "7", "hello"]
 
# Count how many values meet the following condition:
 
# The value must be a valid number and be greater than 5 and less than 15,
# or the value is exactly "abc".
 
# ⚠️ Be careful: some values are not numbers.
 
 
# -----------------------------------------
 
# =========================================
# TASK 17: VIP Queue System
# =========================================
 
# A system decides whether a person can skip the queue.
 
# A person can skip the queue if they are a VIP and not banned, or if
# they have a fast pass and are at least 18 years old, or if they are
# below 12 years old and are accompanied.
 
# Otherwise → "Join normal queue"
 
# 1. Ask for:
#    - is_vip (yes/no)
#    - banned (yes/no)
#    - has_fastpass (yes/no)
#    - age
#    - accompanied (yes/no)
 
 
