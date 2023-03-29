# lameR
Lame and slow way to check R packages for vulnerabilities

<img width="591" alt="Screenshot 2023-03-29 at 08 51 35" src="https://user-images.githubusercontent.com/10061471/228450108-8acdf453-541f-4d25-83c5-a98d368e5eb0.png">
                                


This script will check R package or list of R pakages on ossindex.sonatype.org.
It will report if a package has vulnerabilities, regardless of the version.
Is will also report if ppackage was not found on ossindex so you can do manual checks.
Inspired by oysteR but, generally speaking, slower and lamer way to do the same thing.
The only advantage is that we don't have to install R or any of the packages to
perform these checks.
We don't have to sign up for the ossindex.sonatype.org because we're taking it slow
and going below the rate limiting.

## Example Usage:
#### Check sigle package:
python lameR.py package_name
#### Check lisf of packages:
python lameR.py -f /path/to/package/list

## Example Results
<img width="942" alt="Screenshot 2023-03-29 at 08 53 37" src="https://user-images.githubusercontent.com/10061471/228450596-7ef79c9a-d265-4d4b-a399-4f86d59f10ce.png">
