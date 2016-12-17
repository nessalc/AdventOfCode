require 'digest'
password=ARGV[0]
def valid_directions(password,position)
  x,y=position
  test=Digest::MD5.hexdigest(password)[0,4]
  u='bcdef'.include?(test[0])
  d='bcdef'.include?(test[1])
  l='bcdef'.include?(test[2])
  r='bcdef'.include?(test[3])
  if y==0 then u=false end
  if y==3 then d=false end
  if x==0 then l=false end
  if x==3 then r=false end
  return u,d,l,r
end
$valid_paths=[]
def find_vault(password,position=[0,0])
  if position==[3,3] then
    $valid_paths<<password[ARGV[0].length,password.length]
    return password
  end
  x,y=position
  u,d,l,r=valid_directions(password,position)
  if u then find_vault(password+'U',[x,y-1]) end
  if d then find_vault(password+'D',[x,y+1]) end
  if l then find_vault(password+'L',[x-1,y]) end
  if r then find_vault(password+'R',[x+1,y]) end
  if not [u,d,l,r].any? then return nil end
end
find_vault(password)
test=$valid_paths.map{|p| p.length}
puts "Part 1: The shortest path is #{$valid_paths[test.index(test.min)]} (#{$valid_paths[test.index(test.min)].length} steps)"
puts "Part 2: The longest path is #{$valid_paths[test.index(test.max)]} (#{$valid_paths[test.index(test.max)].length} steps)"