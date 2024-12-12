use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn dfs(num: u64, step: u16, memo: &mut HashMap<(u64, u16), i128>) -> i128 {
    if step == 0 {
        return 1i128;
    }
    let key = (num, step);
    if let Some(value) = memo.get(&key) {
        return *value;
    }
    let mut count: i128 = 0;
    if num == 0 {
        count += dfs(1, step - 1, memo);
    } else if num.to_string().len() % 2 == 0 {
        let s = num.to_string();
        let mid = s.len() / 2;
        if let Ok(val) = &s[..mid].parse::<u64>() {
            count += dfs(*val, step - 1, memo);
        }
        if let Ok(val) = &s[mid..].parse::<u64>() {
            count += dfs(*val, step - 1, memo);
        }
    } else {
        count += dfs(num * 2024, step - 1, memo);
    }
    memo.insert((num, step), count);
    count
}
fn main() {
    let path = Path::new("/Users/keni/code/adventOfCode2024/sample/day11.txt");
    let file = File::open(path).expect("Unable to open file");
    let mut stones: Vec<u64> = Vec::new();

    // Read file and populate `stones`
    for line in io::BufReader::new(file).lines() {
        let line = line.expect("Uable to read line");
        stones = line
            .split_whitespace()
            .map(|num| num.parse::<u64>().unwrap())
            .collect();
    }
    let blinks = 75;
    let mut memo: HashMap<(u64, u16), i128> = HashMap::new();

    let mut result: i128 = 0;
    for &stone in &stones {
        println!("{result}");
        result += dfs(stone, blinks, &mut memo);
    }

    println!("{}", stones.len());
    println!("{result}");
}
