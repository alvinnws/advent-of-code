let rec rl ic n = 
  try
    let line = input_line ic in
    let direction = (String.get line 0) in
    let rotation = int_of_string (String.sub line 1 ((String.length line)-1)) in
    let res = if direction = 'L' then n-rotation else n+rotation in
    if res mod 100 < 0 then
      rl ic ((res mod 100) + 100)
    else if res mod 100 = 0 then
      1 + (rl ic 0)
    else
      rl ic (res mod 100)
  with _e ->
    close_in ic;
    0

let part1 file =
  rl (open_in file) 50