
from esipy import EsiApp
from esipy import EsiClient
from esipy import EsiSecurity

app = EsiApp().get_latest_swagger

# replace the redirect_uri, client_id and secret_key values
# with the values you get from the STEP 1 !
security = EsiSecurity(
    redirect_uri='https://localhost',
    client_id='d3e25426fc70488b824a06152c691d8b',
    secret_key='AL31AMYudSlIoWMrrsav8DNjFXAgLjP2weka8CIU',
    headers={'User-Agent': 'lars@kirkhus.org'},
)

# and the client object, replace the header user agent value with something reliable !
client = EsiClient(
    retry_requests=True,
    headers={'User-Agent': 'lars@kirkhus.org'},
    security=security
)

scopes=[
"publicData", "esi-calendar.respond_calendar_events.v1", "esi-calendar.read_calendar_events.v1", "esi-location.read_location.v1", "esi-location.read_ship_type.v1", "esi-mail.organize_mail.v1", "esi-mail.read_mail.v1", "esi-mail.send_mail.v1", "esi-skills.read_skills.v1", "esi-skills.read_skillqueue.v1", "esi-wallet.read_character_wallet.v1", "esi-wallet.read_corporation_wallet.v1", "esi-search.search_structures.v1", "esi-clones.read_clones.v1", "esi-characters.read_contacts.v1", "esi-universe.read_structures.v1", "esi-bookmarks.read_character_bookmarks.v1", "esi-killmails.read_killmails.v1", "esi-corporations.read_corporation_membership.v1", "esi-assets.read_assets.v1", "esi-planets.manage_planets.v1", "esi-fleets.read_fleet.v1", "esi-fleets.write_fleet.v1", "esi-ui.open_window.v1", "esi-ui.write_waypoint.v1", "esi-characters.write_contacts.v1", "esi-fittings.read_fittings.v1", "esi-fittings.write_fittings.v1", "esi-markets.structure_markets.v1", "esi-corporations.read_structures.v1", "esi-characters.read_loyalty.v1", "esi-characters.read_opportunities.v1", "esi-characters.read_chat_channels.v1", "esi-characters.read_medals.v1", "esi-characters.read_standings.v1", "esi-characters.read_agents_research.v1", "esi-industry.read_character_jobs.v1", "esi-markets.read_character_orders.v1", "esi-characters.read_blueprints.v1", "esi-characters.read_corporation_roles.v1", "esi-location.read_online.v1", "esi-contracts.read_character_contracts.v1", "esi-clones.read_implants.v1", "esi-characters.read_fatigue.v1", "esi-killmails.read_corporation_killmails.v1", "esi-corporations.track_members.v1", "esi-wallet.read_corporation_wallets.v1", "esi-characters.read_notifications.v1", "esi-corporations.read_divisions.v1", "esi-corporations.read_contacts.v1", "esi-assets.read_corporation_assets.v1", "esi-corporations.read_titles.v1", "esi-corporations.read_blueprints.v1", "esi-bookmarks.read_corporation_bookmarks.v1", "esi-contracts.read_corporation_contracts.v1", "esi-corporations.read_standings.v1", "esi-corporations.read_starbases.v1", "esi-industry.read_corporation_jobs.v1", "esi-markets.read_corporation_orders.v1", "esi-corporations.read_container_logs.v1", "esi-industry.read_character_mining.v1", "esi-industry.read_corporation_mining.v1", "esi-planets.read_customs_offices.v1", "esi-corporations.read_facilities.v1", "esi-corporations.read_medals.v1", "esi-characters.read_titles.v1", "esi-alliances.read_contacts.v1", "esi-characters.read_fw_stats.v1", "esi-corporations.read_fw_stats.v1", "esi-characterstats.read.v1"]

print("Paste this url into a web browser: ", security.get_auth_uri(state='RRandom1234Lars', scopes=scopes))



#token_string = '4icQwd-pQESmFp-O13d-Hw'
token_string = "jtkN9ou0406ylWeAJHJkCA"

#refresh_token = '0HbqXkmqtUacnG/l+Qju+w=='

"""
security.update_token({
    'access_token': '',  # leave this empty
    'expires_in': -1,  # seconds until expiry, so we force refresh anyway
    'refresh_token': token_st
})
"""
tokens = security.auth(token_string)

print(tokens)

api_info = security.verify()


