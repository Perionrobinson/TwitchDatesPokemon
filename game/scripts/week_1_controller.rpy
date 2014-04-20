label day_1_after_school_choice:
  "There's nothing to do today"
  return

label day_2_after_school_choice:
  menu:
    "Attend the Science Club meeting":
      call science_club_first_meeting
    "Do nothing":
      "You do nothing."
  return
