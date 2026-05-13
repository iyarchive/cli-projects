select
	title,
  authors,
  date_added,
  last_date_read,
  dates_read,
  moods,
  pace,
  star_rating,
  review
from bookreviews
WHERE read_status == 'read';
