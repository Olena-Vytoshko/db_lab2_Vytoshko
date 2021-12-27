-- get count of draws, black winners and white winners
SELECT winner, count(*)
FROM public.games
GROUP BY winner;

-- get count of rate and non-rate match
SELECT rated, count(*)
FROM public.games
GROUP BY rated;

-- get count of end game types
SELECT game_status, count(*)
FROM public.games
GROUP BY game_status;