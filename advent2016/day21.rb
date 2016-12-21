f=File.open(ARGV[0])
instructions=f.readlines()
passwd=+ARGV[1]
def scramble(tstring,instruction)
  parts=instruction.strip.split
  string=+tstring
  case parts[0]
  when 'swap'
    if parts[1]=='position'
      a,b=parts[2].to_i,parts[5].to_i
    elsif parts[1]=='letter'
      a,b=string.index(parts[2]),string.index(parts[5])
    end
    string[a],string[b]=string[b],string[a]
  when 'rotate'
    if parts[1]=='based'
      idx=string.index(parts[6])
      amount=-idx-1-(idx>=4 ? 1 : 0)
    elsif parts[1]=='left'
      amount=parts[2].to_i
    elsif parts[1]=='right'
      amount=-parts[2].to_i
    end
    string=string.chars.rotate(amount).join
  when 'reverse'
    a,b=parts[2].to_i,parts[4].to_i
    string.insert(a,string.slice!(a,b-a+1).reverse)
  when 'move'
    a,b=parts[2].to_i,parts[5].to_i
    string.insert(b,string.slice!(a))
  end
  return string
end
instructions.each do |instruction|
  passwd=scramble(passwd,instruction)
end
puts "Part 1: Scrambled password is #{passwd}"
passwd=+ARGV[2]
ptest=''
passwd.chars.permutation do |atest|
  ptest=atest.join
  instructions.each do |instruction|
    ptest=scramble(ptest,instruction)
  end
  if ptest==passwd
    puts "Possible password: #{atest.join}"
  end
end

