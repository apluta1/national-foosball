async function loadStandings(filename, elementId) {
    const list = document.getElementById(elementId);

    try {
        const response = await fetch(filename);

        if (!response.ok) {
            throw new Error(`Failed to load ${filename}`);
        }

        const teams = await response.json();

        teams.sort((a, b) => a.rank - b.rank);

        teams.forEach(team => {
            const item = document.createElement("li");
            item.className = "team";

            const rank = document.createElement("div");
            rank.className = "rank";
            rank.textContent = `#${team.rank}`;

            const info = document.createElement("div");
            info.className = "team-info";

            const username = document.createElement("div");
            username.className = "username";
            username.textContent = team.username;

            const stats = document.createElement("div");
            stats.className = "stats";

            [
                ["Wins", team.wins],
                ["Losses", team.losses],
                ["Points", team.points.toLocaleString()]
            ].forEach(([label, value]) => {
                const stat = document.createElement("span");
                stat.className = "stat";

                const strong = document.createElement("strong");
                strong.textContent = value;

                stat.append(`${label}: `);
                stat.appendChild(strong);
                stats.appendChild(stat);
            });

            info.append(username, stats);
            item.append(rank, info);
            list.appendChild(item);
        });

    } catch (error) {
        console.error(error);
        list.textContent = "Unable to load standings.";
    }
}

// Load both JSON files independently
loadStandings(
    "Foosball-Website/national_foosball_standings.json",
    "national-standings"
);

loadStandings(
    "Foosball-Website/national_foosball_standings_jv.json",
    "jv-standings"
);