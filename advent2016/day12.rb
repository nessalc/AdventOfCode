f=File.open(ARGV[0])
program=f.readlines().map { |line| line.strip }
def run_program(program,a=0,b=0,c=0,d=0)
  counter=0
  counter_max=program.length
  while counter<counter_max
    instruction=program[counter].split
    case instruction[0]
    when 'cpy'
      eval instruction[2]+'='+instruction[1]
    when 'inc'
      eval instruction[1]+'+=1'
    when 'dec'
      eval instruction[1]+'-=1'
    when 'jnz'
      test=eval instruction[1]+'!=0'
      if test
        counter+=instruction[2].to_i-1
      end
    end
    counter+=1
  end
  return a,b,c,d
end
a,b,c,d=run_program(program)
puts "Part 1: Register a = #{a}"
a,b,c,d=run_program(program,0,0,1,0)
puts "Part 2: Register a = #{a}"
