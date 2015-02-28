# Enter your code here. Read input from STDIN. Print output to STDOUT
t = gets.to_i
t.times do
    n = gets.to_i
    puts prime_factors(n)
end

def is_prime(num)
  if num < 2
    return false
  else
    square_root = Math.sqrt(num)
    (2..square_root).each do |i|
      if num % i == 0
        return false
      end
    end
  end
  true
end

def prime_factors(num)
  result = []
  result.push(2) if num % 2 == 0
  (3..num).step(2) do |i|
    if is_prime(i) && num % i == 0
      result.push(i)
    end
  end
  result.length
end
