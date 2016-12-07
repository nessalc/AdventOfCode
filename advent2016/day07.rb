f=File.open(ARGV[0])
lines=f.readlines()
count=0
lines.each do |line|
  line.scan(/\[[^\]]*?(\w)(\w)\2\1[^\[]*?\]/).each do |test1|
    unless test1[0]!=test1[1]
      line.scan(/(\w)(\w)\2\1/).each do |test2|
        if test2[0]!=test2[1]
          count+=1
	  break
        end
      end
    else
      break
    end
  end
end
puts "Part 1: #{count} Addresses support TLS"
