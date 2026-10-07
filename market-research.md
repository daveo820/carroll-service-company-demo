# Market research: Carroll Service Company, Garner NC (HVAC)

Checked 7 October 2026. Lighthouse 12, mobile profile, one run each from the same box, so treat single numbers as rough. Screenshots of every site are in `research/` (compressed).

## 1. Is the lead real?

| Lead claim | What I found | Verdict |
|---|---|---|
| Business active | Google status Open, 4.8 from 25 reviews, newest review Feb 2026, 40 permits in 2025 and 6 so far in 2026 on BuildZoom | Holds up |
| Family owned since 1973, owners Lee F. Carroll and son | Site says 1973 and "Lee Carroll and his son Brandon Carroll". BuildZoom lists Lee F. Carroll and Brian Carroll. Van and logo say "Lee, Brian &amp; Brandon Carroll" | Holds up, names need confirming |
| About 580 permits | BuildZoom: 582 all time | Holds up |
| Site is desktop only | No viewport meta tag. On an iPhone 13 the page lays out about 996px wide and is shrunk to fit, so text is tiny and you pinch to read. Lighthouse fails viewport and legible font size | Holds up |
| Runs Drupal 7, no security updates since Jan 2025 | Response header `x-generator: Drupal 7`. Public `/CHANGELOG.txt` lists 7.67 (8 May 2019) as the newest release. Drupal 7 reached end of life on 5 Jan 2025 (drupal.org PSA-2023-06-07, PSA-2025-01-06) | Holds up, and it is worse than the lead said: the changelog suggests core was last updated in 2019, years before end of life. Caveat: the changelog is only a strong hint; only admin access proves the installed version. Hosted on Pantheon |

## 2. Audit of carrollservicecompany.com

Lighthouse mobile: **Performance 91, Accessibility 53, Best Practices 86, SEO 85.** FCP 1.2s, LCP 3.5s, 458 KiB.

Brutal honesty: the site is **fast**. It is small and old, so speed is not the pitch. The pitch is that it does not work on a phone, it is built on unsupported software, and it hides what makes Carroll good.

- No viewport tag, so every phone visitor gets a shrunk desktop page. Font size and viewport audits fail.
- Drupal 7 with a 2019 changelog, past end of life. A public "Admin" link in the footer points at `/user/login`. An "IE6 No More" module (a 2009 era Internet Explorer 6 warning) is still installed.
- No meta description. No `lang` attribute on the page. Color contrast and link name audits fail.
- Six content images (logo, slideshow, the family photo) have blank alt text, so screen readers skip them.
- No schema markup, so nothing tells Google this is an HVAC business with hours, a phone number and 25 reviews.
- The 4.8 Google rating and every Google review are absent. The testimonials page is undated.
- The best photo, the three Carrolls in front of the van, is buried on an inner page.
- Nothing about the maintenance agreement's price or contents, and no estimate form.

## 3. Competitors

| Site | Where | Perf | A11y | BP | SEO | LCP | Weight |
|---|---|---|---|---|---|---|---|
| stephensonheatingandair.com | Garner | 66 | 87 | 96 | 77 | 5.7s | 2.7 MB |
| 919fixmyac.com | Raleigh | 54 | 81 | 96 | 92 | 10.6s | 2.0 MB |
| home-comfort-systems.com | Garner | 47 | 77 | 79 | 92 | 14.5s | 3.6 MB |
| airconditioningrepairraleigh.com (Icy Hot) | Raleigh | 46 | 98 | 79 | 100 | 9.0s | 1.0 MB |
| allhoursheatingair.com | Garner | 43 | 84 | 75 | 85 | 4.0s | 3.3 MB |
| onehourheatandair.com | National franchise | 33 | 81 | 75 | 77 | 12.0s | 2.4 MB |
| servicechampions.net | California, national benchmark | 31 | 92 | 68 | 100 | 32.0s | 6.5 MB |
| thermodirectinc.com | Raleigh Durham | 26 | 89 | 75 | 100 | 21.6s | 23.6 MB |
| modernmechhvac.com | Garner | 8 | 87 | 57 | 85 | 31.5s | 4.8 MB |
| comfortmonsterheating.com | | n/a | | | | | Chrome blocked the load with an interstitial; skipped |
| **carrollservicecompany.com (today)** | Garner | **91** | **53** | 86 | 85 | 3.5s | 0.46 MB |
| **Carroll concept (local, uncompressed)** | | **97** | **100** | **100** | 66* | 2.4s | 116 KiB |

\* SEO is held down on purpose by noindex and the robots.txt block. The only SEO audit it fails is the crawl block (is-crawlable).

### What the strong sites do
1. **Phone and a booking button in the header on every page.** Every Garner competitor does this. Carroll's phone sits in the page body.
2. **Review proof above the fold.** Modern Mechanical (Garner, family owned since 2007) shows "Excellent, 2,297 reviews" as the first line of its hero (its own widget, not checked against Google). Icy Hot shows a 4.9 Google badge. One Hour shows 4.81. Carroll shows nothing.
3. **Family and longevity as a headline.** Modern Mechanical leads with "Family owned home services company operating since 2007." Carroll has 34 more years than that and does not say it until the third paragraph.
4. **A maintenance plan as a product,** with its own name and a sign up page (Service Champions' MVP+ program, for example). Carroll's plan has no name, price or contents on the site.
5. **Financing offer up front.** Modern Mechanical: 60 month financing. Carroll offers Wells Fargo financing, buried.

### What they get wrong (the opening for Carroll)
- Heavy and slow: seven of nine take 9 seconds or more to show the main content on mobile, and Thermo Direct ships 23.6 MB.
- Cookie consent pop ups cover the hero on Modern Mechanical, One Hour, Service Champions and Thermo Direct.
- Doorway page spam: All Hours lists dozens of town pages in its menu ("Auburn HVAC Services", "Auburn Air Conditioning Professionals", and so on).
- Generic stock heroes. Carroll has a real photo of three family members and their van, which no competitor can copy.

## 4. What the concept does with this
- Leads with the family photo, 1973, and the phone number in the header and hero.
- Puts 4.8 from 25 Google reviews and eight real reviews on the page, with sources.
- Turns the maintenance agreement into a product block (price left as a labeled placeholder).
- Shows six real 2025 replacement permit values ($8,200 to $17,800) so buyers see an honest range.
- Proper mobile layout, schema (HVACBusiness, Service, BreadcrumbList), meta descriptions, alt text, and 100 accessibility.

## 5. Risks for the pitch
- **Review count is the weak spot.** 25 Google reviews in 53 years, against a Garner competitor claiming 2,297. A new site will not fix that alone; a review request habit would.
- **2026 volume.** 6 permits through mid September 2026 against 40 in 2025. Could be BuildZoom lag, could be a real slowdown or a succession question in a 53 year old family business. Ask, gently.
- **Names.** Brian vs Brandon: BuildZoom and the logo say Brian, the Our Company page says Brandon, the van says both. Get it right before showing them.
- **Speed is not an argument here.** Their current site scores 91. Pitch phones, security and trust, not speed.
- **License** #10119 is printed on their site but BuildZoom has not re verified it since 2010. Check the state board before quoting it.
