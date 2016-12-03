f=File.open(ARGV[0])
lines=f.readlines()
possible=0
lines.collect!{|s| s.split(' ')}
lines.collect!{|s| s.map{|t| t.to_i}}
lines.each do |sides|
  tsides=sides.sort
  if tsides[0]+tsides[1]>tsides[2]
    possible+=1
  end
end
puts "Part 1: #{possible} possible triangles"
possible=0
while lines.length>=3
  sides=lines.take(3)
  sides=sides.transpose()
  sides.each do |tsides|
    tsides.sort!
    if tsides[0]+tsides[1]>tsides[2]
      possible+=1
    end
  end
  lines=lines.drop(3)
end
puts "Part 2: #{possible} possible triangles"
