$in_50=[]
def is_wall(pos,number)
  x,y=pos
  test=x*x + 3*x + 2*x*y + y + y*y + number
  if test.to_s(2).count('1')%2==1
    return true
  else
    return false
  end
end
def get_valid_moves(visited,pos,number)
  valid_moves=[]
  x,y=pos
  if x-1>=0 and not is_wall([x-1,y],number) and not visited.include?([x-1,y])
    valid_moves<<[x-1,y]
  end
  if y-1>=0 and not is_wall([x,y-1],number) and not visited.include?([x,y-1])
    valid_moves<<[x,y-1]
  end
  if not is_wall([x+1,y],number) and not visited.include?([x+1,y])
    valid_moves<<[x+1,y]
  end
  if not is_wall([x,y+1],number) and not visited.include?([x,y+1])
    valid_moves<<[x,y+1]
  end
  return valid_moves
end
$minlen=100000000
$maxlen=0
$solution_count=0
$oldsolcount=0
def solve_maze(solution,destination,number)
  start=solution[-1]
  valid_moves=get_valid_moves(solution,start,number)
  if solution.length<=51
    solution.each do |pos|
      if not $in_50.include?(pos)
        $in_50<<pos
      end
    end
  end
  if destination==start
    $solution_count+=1
    if solution.length<$minlen
      puts "Shorter solution! #{solution.length-1}" #remove starting block
      $minlen=solution.length-1
    end
    if solution.length>$maxlen
      $maxlen=solution.length-1
    end
    return solution.length
  end
  valid_moves.each do |pos|
    solve_maze(solution+[pos],destination,number)
  end
  if $solution_count>$oldsolcount and $solution_count%100==0
    $oldsolcount=$solution_count
    puts "Solutions scanned: #{$solution_count}"
  end
end
solve_maze([[1,1]],[31,39],ARGV[0].to_i)
puts "Interesting info:"
puts "* there are #{$solution_count} valid solutions for this maze."
puts "* the maximum distance for a solution is #{$maxlen}"
puts "* Part 1: It takes a minimum of #{$minlen} steps to reach 31, 39."
puts "* Part 2: There are #{$in_50.length} distinct locations one can visit in 50 or fewer steps."
