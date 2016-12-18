f=File.open(ARGV[0])
lines=f.readlines()
rows=ARGV[1].to_i
cols=lines[0].length
(1...rows).each do |i|
  line=''
  (0...cols).each do |j|
    if j==0
      l=false
      r=lines[i-1][j+1]=='^'
    elsif j==(cols-1)
      l=lines[i-1][j-1]=='^'
      r=false
    else
      l=lines[i-1][j-1]=='^'
      r=lines[i-1][j+1]=='^'
    end
    c=lines[i-1][j]=='^'
    if (l and c and (not r)) or ((not l) and c and r) or (l and (not c) and (not r)) or ((not l) and (not c) and r)
      line<<'^'
    else
      line<<'.'
    end
  end
  lines<<line
  if i%1000==0
    print '.'
  end
end
print "\n"
#lines.each do |line|
#  puts "|#{line}|"
#end
safe=lines.map{|l| l.count('.')}.reduce(:+)
puts "Safe tiles: #{safe}"
