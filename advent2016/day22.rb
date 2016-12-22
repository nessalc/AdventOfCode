f=File.open(ARGV[0])
lines=f.readlines() #read in file
lines=lines[2,lines.length] #ignore first two lines
$gridsize=/node-x(\d+)-y(\d+)/.match(lines[-1])[1,2].map{|t|t.to_i}
$grid=Array.new($gridsize[0]+1){Array.new($gridsize[1]+1)}
total_space,total_used=0,0
lines.each do |line|
  x,y,size,used=/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T/.match(line)[1,4].map{|t|t.to_i}
  $grid[x][y]={:used => used, :size => size, :avail => size-used}
  total_space+=size
  total_used+=used
end
puts "The Easter Bunny has #{total_space}T storage space, and is using #{total_used}T (%0.2f%%) of it." % ((total_used+0.0)/total_space*100)
viable=0
(0..$gridsize[0]).to_a.product((0..$gridsize[1]).to_a).to_a.repeated_permutation(2).each do |nodes|
  a,b=nodes
  if [a[0],a[1]] != [b[0],b[1]] and $grid[a[0]][a[1]][:used]>0 and $grid[a[0]][a[1]][:used]<=$grid[b[0]][b[1]][:avail]
    viable+=1
  end
end
puts "There are #{viable} viable pairs of nodes."
puts "Goal data is located at /dev/grid/node-x#{$gridsize[0]}-y0"
$goal=$gridsize[0],0
x,y=$gridsize
empty=0,0
(0..x).each do |i|
  (0..y).each do |j|
    node=$grid[i][j]
    if node[:used]==0
      empty=i,j
      puts "Empty node at /dev/grid/node-x#{i}-y#{j}"
    end
  end
end
def check_directions(position,prevdir=nil)
  x,y=position
  node=$grid[x][y]
  directions=[]
  if x>0 and $grid[x-1][y][:used]<=node[:avail] and prevdir != :right
    directions << :left
  end
  if x<$gridsize[0] and $grid[x+1][y][:used]<=node[:avail] and prevdir != :left
    directions << :right
  end
  if y>0 and $grid[x][y-1][:used]<node[:avail] and prevdir != :down
    directions << :up
  end
  if y<$gridsize[1] and $grid[x][y+1][:used]<node[:avail] and prevdir != :up
    directions << :down
  end
  return directions
end
def swap(position,direction)
  x,y=position
  case direction
  when :left
    if [x-1,y]==$goal
      $goal=x,y
      puts "Goal moved to #{x},#{y}"
    end
    $grid[x][y][:used],$grid[x-1][y][:used]=$grid[x-1][y][:used],$grid[x][y][:used]
    $grid[x][y][:avail]=$grid[x][y][:size]-$grid[x][y][:used]
    x-=1
    $grid[x][y][:avail]=$grid[x][y][:size]-$grid[x][y][:used]
  when :right
    if [x+1,y]==$goal
      $goal=x,y
      puts "Goal moved to #{x},#{y}"
    end
    $grid[x][y][:used],$grid[x-1][y][:used]=$grid[x-1][y][:used],$grid[x][y][:used]
    $grid[x][y][:avail]=$grid[x][y][:size]-$grid[x][y][:used]
    x+=1
    $grid[x][y][:avail]=$grid[x][y][:size]-$grid[x][y][:used]
  when :up
    if [x,y-1]==$goal
      $goal=x,y
      puts "Goal moved to #{x},#{y}"
    end
    $grid[x][y][:used],$grid[x-1][y][:used]=$grid[x-1][y][:used],$grid[x][y][:used]
    $grid[x][y][:avail]=$grid[x][y][:size]-$grid[x][y][:used]
    y-=1
    $grid[x][y][:avail]=$grid[x][y][:size]-$grid[x][y][:used]
  when :down
    if [x,y+1]==$goal
      $goal=x,y
      puts "Goal moved to #{x},#{y}"
    end
    $grid[x][y][:used],$grid[x-1][y][:used]=$grid[x-1][y][:used],$grid[x][y][:used]
    $grid[x][y][:avail]=$grid[x][y][:size]-$grid[x][y][:used]
    y+=1
    $grid[x][y][:avail]=$grid[x][y][:size]-$grid[x][y][:used]
  end
  return x,y
end
moves=0
dir=nil
path=[]
opposite={:left=>:right,:right=>:left,:up=>:down,:down=>:up}
until $goal==[0,0]
  dir=check_directions(empty,dir).sample
  if dir==nil and path.length>0
    #puts "Oops! Wrong way!"
    empty=swap(empty,opposite[path.pop])
    next
  elsif dir==nil
    puts "Can't Move!"
    break
  else
    path << dir
  end
  empty=swap(empty,dir)
  moves+=1
  if moves>10
    break
  end
  puts "#{path}"
end
if moves<=10
  puts "Took #{moves} moves"
end
