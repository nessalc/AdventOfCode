f=File.open(ARGV[0])
lines=f.readlines()
discs=[]
lines.each do |line|
  discs<<[line.split[3].to_i,line.split[11].to_i]
end
capsule=false
t=0
until capsule
  capsule=discs.map.with_index{ |x,i| (x[1]+i+t+1)%x[0]==0 }.all?
  t+=1
end
puts "Part 1: Press the button at time #{t-1} to get the capsule."
discs<<[11,0]
capsule=false
t=0
until capsule
  capsule=discs.map.with_index{ |x,i| (x[1]+i+t+1)%x[0]==0 }.all?
  t+=1
end
puts "Part 2: Press the button at time #{t-1} to get the capsule."
