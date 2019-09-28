import csv
import arrow

# Make sure the first line of the csv is the following:
# artist, album, track, date

# Put the csv in the same folder as this py file and put the filename in the next line
your_csv_filename = 'plissk3n.csv'

# Make sure to have python and arrow via pip installed
# 'pip install arrow' or 'pip3 install arrow' should do the trick

def prepare_csv(filename):
    artists = {}
    dates = []

    # Read in all the data
    with open(filename, 'r') as _filehandler:
        csv_file_reader = csv.DictReader(_filehandler)
        for row in csv_file_reader:
            # Read in the csv values for this row
            artist = row['artist']
            month = arrow.get(row['date'], 'DD MMM YYYY HH:mm').format('MMMM')
            year = arrow.get(row['date'], 'DD MMM YYYY HH:mm').format('YYYY')
            date = year + ' ' + month
            
            # Add a new artist to the dict if needed
            if artist not in artists:
                artists[artist] = {}

            # Add a new date to the artists dict with start counter one or
            # if already present add one for this date
            if date not in artists[artist]:
                artists[artist][date] = 1
            else:
                artists[artist][date] += 1

            # Add this date to the list of all dates if needed
            if date not in dates:
                dates.insert(0, date)

    # Accumulate the counts
    artistsSum = {}
    for artist in artists:
        sum = 0
        artistsSum[artist] = {'artist':artist}
        for date in dates:
            if date in artists[artist]:
                # Add overall plays for this artist
                sum += artists[artist][date]
                artistsSum[artist][date] = sum

    print(artistsSum)

    # Write all the data
    dates.insert(0, 'artist')
    with open(filename + "-processed.csv", 'w') as out:
        csvOut = csv.DictWriter(out, dates)
        csvOut.writeheader()
        for artist in artistsSum:
            csvOut.writerow(artistsSum[artist])

prepare_csv(your_csv_filename)
