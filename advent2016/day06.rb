f=File.open(ARGV[0])
lines=f.readlines()
lines.map! { |line| line.strip.chars }
message1=''
message2=''
lines.transpose.each do |line|
  hashmap=Hash.new(0)
  line.each { |c| hashmap[c]+=1 }
  message1+=hashmap.rassoc(hashmap.values.sort.reverse[0])[0]
  message2+=hashmap.rassoc(hashmap.values.sort[0])[0]
end
puts "Part 1: Message reads \"#{message1}\""
puts "Part 2: Message reads \"#{message2}\""
