elves=ARGV[0].to_i
n=Math.log2(elves).to_i+1
elf=elves-2**n+1+elves
puts "Part 1: Elf with all the presents is ##{elf}"
n=Math.log(elves,3)
if n==n.to_i
  elf=elves
else
  n=n.to_i+1
  if elves>3**n-(3**(n-1))
    elf=elves-(3**n-elves)
  else
    elf=elves-(3**n-elves)+((3**n-(3**(n-1)))-elves)
  end
end
puts "Part 2: Elf with all the presents is ##{elf}"
