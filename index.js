import jsonfile from "jsonfile";
import moment from "moment";
import simpleGit from "simple-git";
import random from "random";

const path = "./data.json";

// Configure Git with your email
const git = simpleGit();
git.addConfig('user.email', 'sparshkumar510@gmail.com');
git.addConfig('user.name', 'Alphahubhai');

// Date range configuration
const START_DATE = moment('2024-01-01'); // Start of 2024
const END_DATE = moment('2024-12-31'); // End of 2024 (365 days)
const TOTAL_DAYS = END_DATE.diff(START_DATE, 'days');

const markCommit = (x, y) => {
  const date = moment()
    .subtract(1, "y")
    .add(1, "d")
    .add(x, "w")
    .add(y, "d")
    .format();

  const data = {
    date: date,
  };

  jsonfile.writeFile(path, data, () => {
    git.add([path]).commit(date, { "--date": date }).push();
  });
};

// Generate a random date within the specified range with more randomization
const getRandomDate = () => {
  const randomDays = random.int(0, TOTAL_DAYS);
  const date = START_DATE.clone().add(randomDays, 'days');
  
  // Add random time within work hours (9 AM to 6 PM)
  const hour = random.int(9, 18);
  const minute = random.int(0, 59);
  const second = random.int(0, 59);
  
  date.hour(hour);
  date.minute(minute);
  date.second(second);
  
  return date.format();
};

// Generate multiple commits per day for higher density
const getMultipleDates = (count) => {
  const dates = [];
  for (let i = 0; i < count; i++) {
    const randomDays = random.int(0, TOTAL_DAYS);
    const date = START_DATE.clone().add(randomDays, 'days');
    // Add random time within the day
    date.hour(random.int(9, 18));
    date.minute(random.int(0, 59));
    date.second(random.int(0, 59));
    dates.push(date.format());
  }
  return dates;
};

const makeCommits = (n) => {
  if(n===0) return git.push();
  
  // Create multiple commits per day for higher density
  const commitsPerDay = random.int(1, 5); // 1-5 commits per day
  const remainingCommits = Math.min(commitsPerDay, n);
  
  const date = getRandomDate();
  const data = {
    date: date,
  };
  console.log(`Commit ${n}: ${date} (${remainingCommits} commits today)`);
  jsonfile.writeFile(path, data, () => {
    git.add([path]).commit(date, { "--date": date }, () => {
      if (remainingCommits > 1 && n > 1) {
        // Create additional commits for the same day
        setTimeout(() => makeCommits(n - 1), 100);
      } else {
        makeCommits(n - 1);
      }
    });
  });
};

makeCommits(2000); // Much higher density - 2000 commits!
