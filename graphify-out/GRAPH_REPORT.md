# Graph Report - apple-hig-knowledge-base  (2026-11-18)

## Corpus Check
- 180 files · ~287,883 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: .jsonl 1, .log 1)

## Summary
- 894 nodes · 976 edges · 79 communities (70 shown, 9 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 64 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Scraper Guidelines
- Playing Video Guidelines
- Search Fields Guidelines
- Color Guidelines
- Design Principles Guidelines
- Immersive Experiences Guidelines
- Modality Guidelines
- Widgets Guidelines
- Patterns Guidelines
- Gestures Guidelines
- Machine Learning Guidelines
- App Clips Guidelines
- Shareplay Guidelines
- Technologies Guidelines
- Siri Guidelines
- Icons Guidelines
- Accessibility Guidelines
- Game Center Guidelines
- Sliders Guidelines
- Scroll Views Guidelines
- Segmented Controls Guidelines
- Drag And Drop Guidelines
- Toolbars Guidelines
- The Menu Bar Guidelines
- Pickers Guidelines
- Presentation Guidelines
- Typography Guidelines
- Context Menus Guidelines
- Entering Data Guidelines
- Pointing Devices Guidelines
- Pop Up Buttons Guidelines
- Sf Symbols Guidelines
- Tap To Pay On Iphone Guidelines
- Wallet Guidelines
- Icloud Guidelines
- Maps Guidelines
- Menus Guidelines
- Playing Haptics Guidelines
- Progress Indicators Guidelines
- Sign In With Apple Guidelines
- Tab Bars Guidelines
- Disclosure Controls Guidelines
- Home Screen Quick Actions Guidelines
- File Management Guidelines
- Live Activities Guidelines
- Right To Left Guidelines
- Searching Guidelines
- Split Views Guidelines
- Airplay Guidelines
- App Icons Guidelines
- Collaboration And Sharing Guidelines
- Collections Guidelines
- Gauges Guidelines
- Healthkit Guidelines
- Photo Editing Guidelines
- Ratings And Reviews Guidelines
- Researchkit Guidelines
- Settings Guidelines
- Sidebars Guidelines
- Undo And Redo Guidelines
- Top Shelf Guidelines
- Homekit Guidelines
- Inclusion Guidelines
- Printing Guidelines
- Remotes Guidelines
- Shazamkit Guidelines
- Workouts Guidelines
- Augmented Reality Guidelines
- Carplay Guidelines
- Imessage Apps And Stickers Guidelines
- Nfc Guidelines
- Web Views Guidelines
- Activity Rings Guidelines
- Always On Guidelines
- Boxes Guidelines
- Foundations Guidelines
- Getting Started Guidelines
- Gyro And Accelerometer Guidelines
- Status Guidelines

## God Nodes (most connected - your core abstractions)
1. `Patterns Collection` - 25 edges
2. `Technologies` - 18 edges
3. `crawl()` - 16 edges
4. `The Menu Bar` - 15 edges
5. `Manifest` - 14 edges
6. `Layout` - 12 edges
7. `Machine Learning` - 12 edges
8. `Menus and Actions` - 12 edges
9. `Tab Bars` - 12 edges
10. `Designing for Games` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Action Button Hardware Interaction` --semantically_similar_to--> `Camera Control`  [INFERRED] [semantically similar]
  action-button/index.md → camera-control/index.md
- `Alert Minimization and Sparingness` --semantically_similar_to--> `Action Sheets`  [INFERRED] [semantically similar]
  alerts/index.md → action-sheets/index.md
- `Frictionless App Clip Flow` --semantically_similar_to--> `App Shortcuts`  [INFERRED] [semantically similar]
  app-clips/index.md → app-shortcuts/index.md
- `Apple Pencil Squeeze Gesture` --semantically_similar_to--> `Camera Control Overlay (Slider & Picker)`  [INFERRED] [semantically similar]
  apple-pencil-and-scribble/index.md → camera-control/index.md
- `CareKit UI Views (Tasks, Charts, Contacts)` --semantically_similar_to--> `Charting Data`  [INFERRED] [semantically similar]
  carekit/index.md → charting-data/index.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Hardware Triggered Contextual App Interactions** — action_button_index_action_button, camera_control_index_camera_control, apple_pencil_and_scribble_index_squeeze_gesture [INFERRED 0.85]
- **Modal Confirmation and Task Disruption Patterns** — alerts_index_alerts, action_sheets_index_action_sheets, activity_views_index_activity_views [INFERRED 0.85]
- **Lightweight Modular App Surfaces and Extensions** — app_clips_index_app_clips, app_shortcuts_index_app_shortcuts, activity_views_index_share_and_action_extensions [INFERRED 0.85]
- **Apple Platform Design Guidance Suite** — designing_for_ios_index_designing_for_ios, designing_for_ipados_index_designing_for_ipados, designing_for_macos_index_designing_for_macos, designing_for_tvos_index_designing_for_tvos, designing_for_visionos_index_designing_for_visionos, designing_for_watchos_index_designing_for_watchos, designing_for_iphone_duo_index_designing_for_iphone_duo [EXTRACTED 1.00]
- **Core Human Interface Design Principles** — design_principles_index_principle_purpose, design_principles_index_principle_agency, design_principles_index_principle_responsibility, design_principles_index_principle_familiarity, design_principles_index_principle_flexibility, design_principles_index_principle_simplicity, design_principles_index_principle_craft, design_principles_index_principle_delight [EXTRACTED 1.00]
- **watchOS Accessory and Complication Layout Families** — complications_index_circular_family, complications_index_corner_family, complications_index_inline_family, complications_index_rectangular_family [EXTRACTED 1.00]
- **visionOS Spatial Interaction System** — eyes_index_eyes_input, gestures_index_visionos_gestures, digital_crown_index_visionos_immersion_control [INFERRED 0.85]
- **Apple Gaming Integration Architecture** — game_center_index_game_center, game_controls_index_game_controls, game_center_index_game_overlay [EXTRACTED 1.00]
- **Sensitive Credential Input Protection Pattern** — digit_entry_views_index_secure_digit_fields, entering_data_index_secure_text_entry, entering_data_index_securefield [INFERRED 0.95]
- **visionOS Spatial Visual Presentation Architecture** — immersive_experiences_index_immersion_styles, images_index_visionos_spatial_imagery, layout_index_visionos_spatial_layout, image_views_index_visionos_image_presentation [INFERRED 0.85]
- **Perceived App Performance and Responsiveness Pattern** — launching_index_instant_launch, launching_index_launch_screens, loading_index_perceived_loading_speed, loading_index_background_asset_downloads [INFERRED 0.85]
- **Inclusive and Accessible Interaction Foundations** — keyboards_index_full_keyboard_access, inclusion_index_accessibility_spectrum, labels_index_semantic_label_colors [INFERRED 0.85]
- **visionOS Spatial Window and Control Architecture** — materials_index_visionos_glass, ornaments_index_spatial_floating, multitasking_index_visionos_shared_space, menus_index_visionos_breakthrough [INFERRED 0.85]
- **Machine Learning Human-in-the-Loop Feedback and Adaptation Flow** — machine_learning_index_explicit_feedback, machine_learning_index_implicit_feedback, machine_learning_index_corrections, machine_learning_index_calibration [EXTRACTED 1.00]
- **Progressive User Guidance and Contextual Help Framework** — offering_help_index_tips, onboarding_index_interactive_learning, offering_help_index_tooltips [INFERRED 0.85]
- **HIG Value and Action Selection Controls** — pickers_index_pickers, pop_up_buttons_index_pop_up_buttons, pull_down_buttons_index_pull_down_buttons [INFERRED 0.85]
- **Multimedia and Sensory Playback Experience** — playing_audio_index_playing_audio, playing_video_index_playing_video, playing_haptics_index_playing_haptics [INFERRED 0.85]
- **visionOS Spatial Interaction & Feedback** — playing_audio_index_spatial_audio, scroll_views_index_look_to_scroll, privacy_index_visionos_input_privacy [INFERRED 0.85]
- **Hierarchical App Navigation Controls Pattern** — sidebars_index_sidebar_navigation, tab_bars_index_tab_bar_navigation, split_views_index_split_view_panes, tab_views_index_tab_view_panes [INFERRED 0.85]
- **System Intelligence & Multimodal Intent Architecture** — siri_index_siri_ai, snippets_index_snippet_control, siri_index_app_intents_and_entities, searching_index_systemwide_search [INFERRED 0.85]
- **Spatial Computing & Presence Architecture** — spatial_layout_index_field_of_view, spatial_layout_index_depth_perception, shareplay_index_spatial_templates, shareplay_index_spatial_personas [INFERRED 0.85]
- **Text Entry and Input Component Architecture** — text_fields_index_text_fields, text_views_index_text_views, token_fields_index_token_fields, virtual_keyboards_index_virtual_keyboards [INFERRED 0.95]
- **visionOS Spatial Presentation Framework** — windows_index_windows, windows_index_volumetric_windows, widgets_index_visionos_spatial_widgets, toolbars_index_visionos_toolbar [INFERRED 0.85]
- **Apple Wallet Digital Identity and Passes Ecosystem** — wallet_index_wallet, wallet_index_passes, wallet_index_identity_verification, wallet_index_order_tracking [EXTRACTED 1.00]

## Communities (79 total, 9 thin omitted)

### Community 0 - "Scraper Guidelines"
Cohesion: 0.05
Nodes (25): BlockedURLError, _enforce_blocklist(), fetch(), _get_session(), _rate_limit(), Manifest, _now(), _is_blocked() (+17 more)

### Community 1 - "Playing Video Guidelines"
Cohesion: 0.04
Nodes (42): HIG Foundations of Design, Human Interface Guidelines Root, HIG Structural Topics Hierarchy, Apple Hardware Input Modalities, Inputs, Spatial, Eye, and Hand Tracking Inputs, Full Keyboard Access (FKA), Keyboards (+34 more)

### Community 2 - "Search Fields Guidelines"
Cohesion: 0.05
Nodes (33): Navigation and Search, Primary Column Data Hierarchy, Outline Views, NSPathControl, Path Controls, Pop-up Path Control, Standard Path Control, NSSearchField (+25 more)

### Community 3 - "Color Guidelines"
Cohesion: 0.06
Nodes (39): Audio Graphs, Chart Axes, Chart Accessibility, Charts, Chart Marks, Swift Charts, App Accent Colors, Color (+31 more)

### Community 4 - "Design Principles Guidelines"
Cohesion: 0.06
Nodes (31): Design Principles, Designing for Games, Game Center Integration, Game Controls and Inputs, Game Display Adaptation, Game Onboarding and Tutorials, Designing for iOS, iOS Platform Characteristics (+23 more)

### Community 5 - "Immersive Experiences Guidelines"
Cohesion: 0.06
Nodes (28): Feedback, Status feedback, visionOS Custom Environments and Ground Plane, visionOS Immersion Styles (Mixed, Progressive, Full), Immersive Experiences, visionOS Shared Space vs Full Space, Virtual Hands Representation, System Launch Screens (+20 more)

### Community 6 - "Modality Guidelines"
Cohesion: 0.08
Nodes (23): Action Sheets, Destructive Action Presentation, Alert Button Conventions, Alert Minimization and Sparingness, Alerts, Button Semantic Roles, Button Visual Styles and Prominence, Buttons (+15 more)

### Community 7 - "Widgets Guidelines"
Cohesion: 0.07
Nodes (27): Liquid Glass Variants, HUD-Style Panels, Inspector and Auxiliary Panels, Panels, Checkbox, Radio Buttons, Switch Toggle, Toggle-Style Button (+19 more)

### Community 8 - "Patterns Guidelines"
Cohesion: 0.08
Nodes (26): Pattern: Charting Data, Pattern: Collaboration and Sharing, Pattern: Drag and Drop, Pattern: Entering Data, Pattern: Feedback, Pattern: File Management, Pattern: Going Full Screen, Pattern: Launching (+18 more)

### Community 9 - "Gestures Guidelines"
Cohesion: 0.08
Nodes (24): Digital Crown, Digital Crown Navigation, Digital Crown Haptic Detents, Digital Crown Immersion Control, WKCrownDelegate, Custom hover effects, Eyes input, Hover effect (+16 more)

### Community 10 - "Machine Learning Guidelines"
Cohesion: 0.09
Nodes (21): AI transparency and user control, CoreAI framework, FoundationModels framework, Generative AI, Attribution, Calibration, Confidence Communication, Guided and Freeform Corrections (+13 more)

### Community 11 - "App Clips Guidelines"
Cohesion: 0.09
Nodes (22): Action Button, Action Button Hardware Interaction, Action Button Secondary Action, App Clip Card, App Clip Code, App Clips, Frictionless App Clip Flow, App Intents Framework (+14 more)

### Community 12 - "Shareplay Guidelines"
Cohesion: 0.10
Nodes (18): Hierarchical Rendering Mode, Symbol Rendering Modes, SharePlay, Custom Spatial Templates & Seating, GroupActivities Framework, Shared Activities Synchronization, Spatial Personas Presence, visionOS Spatial Seating Templates (+10 more)

### Community 13 - "Technologies Guidelines"
Cohesion: 0.11
Nodes (19): AirPlay, Always On Display, App Clips, Apple In-App Purchase, Apple Pay, Augmented Reality, CareKit, CarPlay (+11 more)

### Community 14 - "Siri Guidelines"
Cohesion: 0.12
Nodes (15): Siri, App Intents and Entities, App Schema Domains, AppIntents Framework, Contextual Cues & View Annotation, Siri AI & Apple Intelligence, Snippets, AppIntents Snippet View API (+7 more)

### Community 15 - "Icons Guidelines"
Cohesion: 0.13
Nodes (13): Icons, Interface Icons and Glyphs, macOS Document Icons, Image Views, visionOS 2D and Spatial Image Presentation, Editable macOS Image Well Interaction, Image Wells, Images (+5 more)

### Community 16 - "Accessibility Guidelines"
Cohesion: 0.15
Nodes (13): Accessibility, Assistive Access, Cognitive Accessibility, Hearing Accessibility, Mobility and Motor Accessibility, Speech Accessibility, Vision Accessibility, CareKit (+5 more)

### Community 17 - "Game Center Guidelines"
Cohesion: 0.17
Nodes (13): Game Center access point, Game Center achievements, Game Center challenges, Game Center, Game Overlay, GameKit, Game Center leaderboards, Game Center multiplayer activities (+5 more)

### Community 18 - "Sliders Guidelines"
Cohesion: 0.18
Nodes (11): Selection and Input, Selection & Input UI Group, Sliders, Circular Sliders, Slider Control & Thumb, Tick Marks & Live Feedback, UISlider, NSSlider & Slider, Steppers (+3 more)

### Community 19 - "Scroll Views Guidelines"
Cohesion: 0.17
Nodes (11): Custom Indicator Images, Flat Sequential Navigation, Page Controls, watchOS Vertical Pagination, visionOS Look to Scroll, NSScrollView, Scroll Edge Effects, Scroll Views (+3 more)

### Community 20 - "Segmented Controls Guidelines"
Cohesion: 0.20
Nodes (9): Segmented Controls, Segmented Control, Spring Loading, Subview Switching, UISegmentedControl & NSSegmentedControl, Tab Views, NSTabView & SwiftUI TabView, Mutually Exclusive Content Panes (+1 more)

### Community 21 - "Drag And Drop Guidelines"
Cohesion: 0.20
Nodes (10): AppKit Drag and Drop, Clipping, Drag and drop, Drag flocking, Spring loading, UIKit Drag and Drop, Edit menus, NSMenu (+2 more)

### Community 22 - "Toolbars Guidelines"
Cohesion: 0.20
Nodes (9): Ornaments, Parallel Plane Floating Structure, Navigation Bar, Prominent Toolbar Action, Toolbar Item Groupings, Toolbar Overflow Menu, Toolbars, visionOS Toolbar (+1 more)

### Community 23 - "The Menu Bar Guidelines"
Cohesion: 0.20
Nodes (10): App Menu, Dynamic Menu Items, File Menu, Format Menu, Help Menu, iPadOS Menu Bar, Menu Bar Extras, The Menu Bar (+2 more)

### Community 24 - "Pickers Guidelines"
Cohesion: 0.25
Nodes (9): Compact Date Picker Style, Date Pickers, NSDatePicker, Pickers, SwiftUI Picker, UIDatePicker, UIPickerView, watchOS Picker (+1 more)

### Community 25 - "Presentation Guidelines"
Cohesion: 0.22
Nodes (9): Presentation: Action Sheets, Presentation: Alerts, Presentation: Page Controls, Presentation: Panels, Presentation: Popovers, Presentation Collection, Presentation: Scroll Views, Presentation: Sheets (+1 more)

### Community 26 - "Typography Guidelines"
Cohesion: 0.22
Nodes (8): Dynamic Tracking, Dynamic Type, New York (NY), San Francisco (SF), Symbolic Traits, System Text Styles, Typography, Variable Fonts & Optical Sizing

### Community 27 - "Context Menus Guidelines"
Cohesion: 0.25
Nodes (8): Context Menu Interaction, Context Menu Preview, Context Menus, Destructive Menu Items, Action Button Control Integration, Control Center Controls, Controls, Locked Camera Capture Control

### Community 28 - "Entering Data Guidelines"
Cohesion: 0.29
Nodes (8): Digit entry views, Secure digit fields, TVDigitEntryViewController, Dynamic validation, Entering data, Expansion tooltip, Secure text entry, SecureField

### Community 29 - "Pointing Devices Guidelines"
Cohesion: 0.25
Nodes (7): iPadOS Pointer Effects, macOS Pointer Styles, NSCursor, Pointer Accessories, Pointing Devices, UIBandSelectionInteraction, UIPointerAccessory

### Community 30 - "Pop Up Buttons Guidelines"
Cohesion: 0.25
Nodes (8): Mutually Exclusive Options, NSPopUpButton, Pop-up Buttons, MenuPickerStyle, Action Menus, NSPopUpButton pullsDown, Pull-down Buttons, showsMenuAsPrimaryAction

### Community 31 - "Sf Symbols Guidelines"
Cohesion: 0.25
Nodes (8): SF Symbols, Custom SF Symbols & Layer Annotation, Design Variants (Fill, Slash, Enclosed), Magic Replace Animation, Symbol Animations Framework, Symbols Framework & SymbolEffect, Variable Color, Symbol Weights and Scales

### Community 32 - "Tap To Pay On Iphone Guidelines"
Cohesion: 0.25
Nodes (6): Tap to Pay on iPhone, Transaction Authorization & Digital Receipts, Tap to Pay Button Branding Rules, Contactless Payment Acceptance, Nonpayment Card Reading & Loyalty, ProximityReader Framework

### Community 33 - "Wallet Guidelines"
Cohesion: 0.25
Nodes (8): Identity Verification with Wallet, Wallet Order Tracking, Pass Designer, Pass Image Specifications, Pass Styles, Wallet Passes, Verify with Apple Wallet Button, Apple Wallet

### Community 34 - "Icloud Guidelines"
Cohesion: 0.29
Nodes (5): GameSave iCloud Synchronization, iCloud, iCloud Storage and Conflict Resolution, Display Only vs Data Transfer Requests, ID Verifier

### Community 35 - "Maps Guidelines"
Cohesion: 0.29
Nodes (6): Map Emphasis Styles, Indoor Maps, Maps, Map Overlays and Annotations, Place Cards, POI Clustering

### Community 36 - "Menus Guidelines"
Cohesion: 0.29
Nodes (6): Menu Item Icons, iOS/iPadOS Menu Layouts, Menus, Submenus, Toggled Menu Items, visionOS Breakthrough Effect for Menus

### Community 37 - "Playing Haptics Guidelines"
Cohesion: 0.33
Nodes (7): CoreHaptics, Custom Haptics, Predefined Feedback Generator, NSHapticFeedbackPerformer, Playing Haptics, UIFeedbackGenerator, watchOS Haptic Detents

### Community 38 - "Progress Indicators Guidelines"
Cohesion: 0.33
Nodes (7): Determinate Progress, Indeterminate Activity Indicators, NSProgressIndicator, Progress Indicators, Refresh Content Controls, ProgressView, UIRefreshControl

### Community 39 - "Sign In With Apple Guidelines"
Cohesion: 0.29
Nodes (5): Sign in with Apple, Biometric Authentication & Privacy, AuthenticationServices & ASAuthorizationAppleIDButton, Private Email Relay Service, System-Provided SIWA Buttons

### Community 40 - "Tab Bars Guidelines"
Cohesion: 0.29
Nodes (6): Tab Bars, Floating Tab Bar on Liquid Glass, iPadOS Sidebar Adaptability, Top-Level Tab Bar Navigation, UITabBar & TabView, visionOS Vertical Expanding Tab Bar

### Community 41 - "Disclosure Controls Guidelines"
Cohesion: 0.33
Nodes (6): Disclosure button, Disclosure controls, Disclosure triangle, DisclosureGroup, NSButton BezelStyle disclosure, NSButton BezelStyle pushDisclosure

### Community 42 - "Home Screen Quick Actions Guidelines"
Cohesion: 0.40
Nodes (6): applicationDockMenu(_:), Dock menus, Dynamic quick actions, Home Screen quick actions, Quick action interface icons, Menus and Actions

### Community 43 - "File Management Guidelines"
Cohesion: 0.33
Nodes (6): Document launcher, DocumentGroupLaunchScene, File management, File provider app extension, Finder Sync extensions, Quick Look previews

### Community 44 - "Live Activities Guidelines"
Cohesion: 0.33
Nodes (5): Live Activity Lifecycle and Timely Updates, Dynamic Island Compact, Minimal, and Expanded Presentations, Live Activities, Lock Screen and StandBy Presentations, Multiplatform Live Activities Distribution

### Community 45 - "Right To Left Guidelines"
Cohesion: 0.40
Nodes (6): Directional Control Flipping, Interface Icon Directionality, RTL Numeral Systems, Right to Left (RTL), SF Symbols RTL Variants, RTL Text Alignment

### Community 46 - "Searching Guidelines"
Cohesion: 0.33
Nodes (5): Searching, Core Spotlight Framework, Search Field Placement, Search Suggestions & History, Spotlight Systemwide Search

### Community 47 - "Split Views Guidelines"
Cohesion: 0.33
Nodes (5): Split Views, Thin Divider Styling & Resizing, Platform Split View Adaptations, Split View Multi-Pane Navigation, UISplitViewController & NavigationSplitView

### Community 48 - "Airplay Guidelines"
Cohesion: 0.40
Nodes (5): Activity Views (Share Sheet), Share and Action Extensions, AirPlay, AirPlay Icon Usage and Branding, AirPlay Playback Continuity

### Community 49 - "App Icons Guidelines"
Cohesion: 0.40
Nodes (5): App Icons, App Icon Appearance Variants, Layered App Icon Architecture, Branding, Subtle Brand Integration

### Community 50 - "Collaboration And Sharing Guidelines"
Cohesion: 0.60
Nodes (5): Collaboration and Sharing, Collaboration Button, Collaboration Popover, Share Button, Share Sheet

### Community 51 - "Collections Guidelines"
Cohesion: 0.50
Nodes (5): Collection Views, Collections, Collection Grid Layout, Browser (Column View), Column Views

### Community 52 - "Gauges Guidelines"
Cohesion: 0.40
Nodes (5): Gauge accessory variant, Gauges, Level indicators, NSLevelIndicator, Gauge

### Community 53 - "Healthkit Guidelines"
Cohesion: 0.40
Nodes (4): Activity rings, Apple Health icon, HealthKit, HKActivityRingView

### Community 54 - "Photo Editing Guidelines"
Cohesion: 0.40
Nodes (4): App Extensions, Photo Editing, Photo Editing Extensions, PhotoKit

### Community 55 - "Ratings And Reviews Guidelines"
Cohesion: 0.40
Nodes (5): NSLevelIndicator.Style.rating, Rating Indicators, Ratings and Reviews, Request Review Prompt, RequestReviewAction

### Community 56 - "Researchkit Guidelines"
Cohesion: 0.50
Nodes (5): Active Tasks & Surveys, HealthKit, Informed Consent & Quizzes, ResearchKit Onboarding Flow, ResearchKit

### Community 57 - "Settings Guidelines"
Cohesion: 0.40
Nodes (3): Settings, macOS Settings Window & Panes, SwiftUI Settings API & UserDefaults

### Community 58 - "Sidebars Guidelines"
Cohesion: 0.40
Nodes (5): Sidebars, Adaptable Sidebar Style, Liquid Glass Background Extension, NavigationSplitView & UICollectionLayoutListConfiguration, Sidebar Navigation Hierarchy

### Community 59 - "Undo And Redo Guidelines"
Cohesion: 0.40
Nodes (3): Edit Menu, Shake to Undo, Undo and Redo

### Community 60 - "Top Shelf Guidelines"
Cohesion: 0.40
Nodes (5): Carousel Actions Layout, Carousel Details Layout, Scrolling Inset Banner, Sectioned Content Row, Top Shelf

### Community 61 - "Homekit Guidelines"
Cohesion: 0.50
Nodes (3): HomeKit Object Model Hierarchy, HomeKit, HomeKit Scenes and Automations

### Community 63 - "Printing Guidelines"
Cohesion: 0.50
Nodes (4): NSDocument, Page Setup Dialog, Printing, UIPrintInteractionController

### Community 64 - "Remotes Guidelines"
Cohesion: 0.50
Nodes (4): Clickpad Gestures, EPG & Channel Navigation, Remotes (Siri Remote), TVServices

### Community 65 - "Shazamkit Guidelines"
Cohesion: 0.50
Nodes (3): ShazamKit, ShazamKit Audio Recognition, ShazamKit Framework

### Community 66 - "Workouts Guidelines"
Cohesion: 0.50
Nodes (4): Activity Rings Summary, Workout Metrics Screen, Workout Sessions, Workouts

### Community 67 - "Augmented Reality Guidelines"
Cohesion: 0.67
Nodes (3): Augmented Reality, AR Coaching Overlay, AR Direct Manipulation

### Community 68 - "Carplay Guidelines"
Cohesion: 0.67
Nodes (3): CarPlay, CarPlay Audio Session Management, Driver Safety and Glanceable Layout

### Community 69 - "Imessage Apps And Stickers Guidelines"
Cohesion: 0.67
Nodes (3): iMessage Apps and Stickers, iMessage Compact vs Expanded Presentation, iMessage Sticker Packs and Specifications

### Community 70 - "Nfc Guidelines"
Cohesion: 0.67
Nodes (3): Background Tag Reading, In-App NFC Tag Reading, NFC (Near-Field Communication)

## Knowledge Gaps
- **469 isolated node(s):** `Vision Accessibility`, `Hearing Accessibility`, `Mobility and Motor Accessibility`, `Speech Accessibility`, `Assistive Access` (+464 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 573 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Layout` connect `Playing Video Guidelines` to `Design Principles Guidelines`, `Immersive Experiences Guidelines`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `crawl()` (e.g. with `BlockedURLError` and `Manifest`) actually correct?**
  _`crawl()` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Vision Accessibility`, `Hearing Accessibility`, `Mobility and Motor Accessibility` to the rest of the system?**
  _469 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Scraper Guidelines` be split into smaller, more focused modules?**
  _Cohesion score 0.05369369369369369 - nodes in this community are weakly interconnected._
- **Why does `Windows` connect `Widgets Guidelines` to `Playing Video Guidelines`, `Toolbars Guidelines`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Manifest` (e.g. with `PageMeta` and `crawl()`) actually correct?**
  _`Manifest` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `Playing Video Guidelines` be split into smaller, more focused modules?**
  _Cohesion score 0.044326241134751775 - nodes in this community are weakly interconnected._