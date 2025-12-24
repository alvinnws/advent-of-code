let rec rl ic n = 
  try
    let line = input_line ic in
    let direction = (String.get line 0) in
    let rotation = int_of_string (String.sub line 1 ((String.length line)-1)) in
    let result = if direction = 'L' then (n-rotation) mod 100 else (n+rotation) mod 100 in
    if result < 0 then
      rl ic (result + 100)
    else if result = 0 then
      1 + (rl ic 0)
    else
      rl ic result
  with _e ->
    close_in ic;
    0

let part1 file =
  rl (open_in file) 50