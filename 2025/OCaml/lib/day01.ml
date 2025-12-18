let rec rl ic n = 
  try
    let line = input_line ic in
    let direction = (String.get line 0) in
    let rotation = int_of_string (String.sub line 1 ((String.length line)-1)) in
    if direction = 'L' then
      let res = (n-rotation) in 
      if res < 0 then
        let res2 = ((res mod 100) + 100) in
        if res2 = 100 then 
          1+(rl ic 0)
        else
          rl ic res2
      else if res = 0 then
        1+(rl ic 0)
      else
        rl ic res
    else
      let res = (n+rotation) in 
      if res > 100 then
        let res2 = (res mod 100) in
          if res2 = 0 then 
            1+(rl ic 0)
          else
            rl ic res2
      else if res = 100 then
        1+(rl ic 0)
      else
        rl ic res
  with _e ->
    close_in ic;
    0
    
let part1 file =
  rl (open_in file) 50