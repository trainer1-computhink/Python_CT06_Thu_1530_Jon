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
 
 # =========================================
# TASK 18: Online Order Approval System
# =========================================

# An online store decides whether to approve an order.

# An order is approved if the customer is not blacklisted and the order
# amount is at least 50 dollars, or if the customer is a premium member.

# However, if the order amount is more than 500 dollars and the customer
# is not a premium member, the order must be rejected.

# Otherwise → "Order Rejected"

# 1. Ask for:
#    - order_amount
#    - premium_member (yes/no)
#    - blacklisted (yes/no)


# -----------------------------------------

# =========================================
# TASK 19: School Attendance Warning System
# =========================================

# A student will receive a warning.

# A warning is issued if the student's attendance is below 75 percent
# and their homework completion is below 60 percent, or if their
# attendance is below 50 percent.

# However, if the student has a valid medical reason, no warning
# should be given.

# Otherwise → "No Warning"

# 1. Ask for:
#    - attendance
#    - homework_completion
#    - medical_reason (yes/no)


# -----------------------------------------

# =========================================
# TASK 20: Secure File Access System
# =========================================

# A user can access a secure file.

# Access is granted if the user is logged in and has admin rights,
# or if the user has a valid access code and is not suspended.

# However, if the user is suspended, they should not be allowed access
# even if they meet other conditions.

# Otherwise → "Access Denied"

# 1. Ask for:
#    - logged_in (yes/no)
#    - admin (yes/no)
#    - access_code_valid (yes/no)
#    - suspended (yes/no)


# -----------------------------------------

# =========================================
# TASK 21: Ride Entry System
# =========================================

# A theme park ride allows entry based on safety rules.

# A person can enter the ride if they are at least 140 cm tall and at
# least 12 years old, or if they are at least 120 cm tall and are
# accompanied by an adult.

# However, if the person has a medical condition, they are not allowed
# to enter regardless of other conditions.

# Otherwise → "Entry Denied"

# 1. Ask for:
#    - height
#    - age
#    - accompanied (yes/no)
#    - medical_condition (yes/no)


# -----------------------------------------

# =========================================
# TASK 22: Gaming Reward System
# =========================================

# A player receives a reward.

# A reward is given if the player scores at least 1000 points and
# completes the level, or if the player finds a secret item.

# However, if the player is flagged for cheating, they should not
# receive any reward even if they meet other conditions.

# Otherwise → "No Reward"

# 1. Ask for:
#    - score
#    - level_completed (yes/no)
#    - found_secret (yes/no)
#    - cheating (yes/no)
