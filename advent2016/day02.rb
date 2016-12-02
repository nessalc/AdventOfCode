f=File.open(ARGV[0])
directions=f.readlines
number=5
code=''
directions.each do |d|
  d.chars.each do |c|
    if c=='U' and not (1..3).include? number then
      number-=3
    elsif c=='D' and not (7..9).include? number then
      number+=3
    elsif c=='L' and not [1,4,7].include? number then
      number-=1
    elsif c=='R' and not [3,6,9].include? number then
      number+=1
    elsif c=="\n"
      code+=number.to_s
    end
  end
end
code+=number.to_s
puts "Part 1: #{code}"
