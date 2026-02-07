# Implementation Plan: Dark Theme Modernization

## Overview

This implementation plan outlines the step-by-step approach to modernize the FINDR parking prediction application with a Dark Slate with Emerald color scheme. The implementation focuses on updating CSS files to use a centralized variable system while maintaining all existing functionality, animations, and responsive behavior.

## Tasks

- [ ] 1. Set up CSS variable system in both CSS files
  - Update `:root` selector in `frontend/src/pages/LandingPage.css` with all required CSS custom properties
  - Update `:root` selector in `frontend/src/pages/MainPage.css` with identical CSS custom properties
  - Add inline comments documenting each variable's purpose
  - Include fallback values for older browser compatibility
  - _Requirements: 1.2, 1.4, 15.1, 15.5_

- [ ] 2. Update Landing Page navigation component styling
  - [ ] 2.1 Update `.landing-nav` to use `var(--surface)` for background with 98% opacity
    - Modify background property to use CSS variable
    - Maintain backdrop-filter blur effect
    - Update border-bottom to use `var(--border)`
    - _Requirements: 2.1, 2.5_
  
  - [ ] 2.2 Update navigation links and text colors
    - Modify `.nav-link` to use `var(--text)` for default color
    - Update `.nav-link:hover` to use `var(--primary)` for hover color
    - Update `.nav-link::after` to use `var(--primary)` for underline effect
    - Modify `.nav-stat` to use `var(--text-muted)` for statistics text
    - Update `.nav-stat-dot` to use `var(--primary)` for emphasis
    - _Requirements: 2.2, 2.3, 2.6_
  
  - [ ] 2.3 Update navigation button styling
    - Modify `.nav-btn` to use `var(--primary)` for background
    - Update button text color to use `var(--background)` for contrast
    - Update `:hover` state to use `var(--primary-dark)`
    - _Requirements: 2.3, 6.1_

- [ ] 3. Update Landing Page hero section styling
  - [ ] 3.1 Update hero section background and gradients
    - Modify `.hero-section` background gradient to use `var(--primary)`, `var(--primary-light)`, and `var(--surface)`
    - Update overlay gradient for text readability
    - Ensure gradient transitions smoothly
    - _Requirements: 3.1, 10.1_
  
  - [ ] 3.2 Update hero text colors
    - Modify `.hero-title` to use `var(--text)` for title color
    - Update `.hero-subtitle` to use `var(--text)` for subtitle color
    - Maintain `.hero-gradient` for accent text (keep existing gradient)
    - _Requirements: 3.2, 3.3_
  
  - [ ] 3.3 Update hero floating cards
    - Modify `.visual-card` to use `var(--surface)` for background
    - Update `.card-title` to use `var(--text)`
    - Update `.card-status` to use `var(--text-muted)`
    - Adjust box-shadow for dark theme visibility
    - _Requirements: 3.4_
  
  - [ ] 3.4 Update hero CTA buttons
    - Modify `.btn-primary` to use `var(--primary)` for background
    - Update button text to use `var(--background)` for contrast
    - Update `:hover` state to use `var(--primary-dark)`
    - Modify `.btn-secondary` to use transparent background with `var(--primary)` border
    - Update `.btn-secondary` text to use `var(--text)`
    - Update `.btn-secondary:hover` to use `var(--primary)` background
    - _Requirements: 3.6, 6.1, 6.4_

- [ ] 4. Update Landing Page card components
  - [ ] 4.1 Update feature cards styling
    - Modify `.feature-card` to use `var(--surface)` for background
    - Update border to use `var(--border)`
    - Adjust box-shadow for dark theme (lighter, more subtle)
    - Update `.feature-card h3` to use `var(--text)`
    - Update `.feature-card p` to use `var(--text-muted)`
    - _Requirements: 4.1, 4.2, 4.4, 4.5_
  
  - [ ] 4.2 Update feature card hover states
    - Modify `.feature-card:hover` border-color to use `var(--primary)`
    - Adjust hover box-shadow with primary color tint
    - Maintain transform effect
    - _Requirements: 4.3_
  
  - [ ] 4.3 Update step cards in "How It Works" section
    - Modify `.step h3` to use `var(--text)`
    - Update `.step p` to use `var(--text-muted)`
    - Maintain `.step-number` gradient with `var(--primary)` and `var(--primary-light)`
    - _Requirements: 4.1, 4.4_

- [ ] 5. Update Landing Page form and modal components
  - [ ] 5.1 Update authentication modal styling
    - Modify `.auth-modal` backdrop to use `var(--overlay)`
    - Update `.auth-content` to use `var(--surface)` for background
    - Add border using `var(--border)`
    - Update `.auth-header h2` to use `var(--text)`
    - Update `.auth-header p` to use `var(--text-muted)`
    - _Requirements: 7.1, 7.2, 7.3_
  
  - [ ] 5.2 Update modal form inputs
    - Modify `.form-group label` to use `var(--text)`
    - Update `.form-group input` to use `var(--surface)` for background
    - Update input text color to use `var(--text)`
    - Update input border to use `var(--border)`
    - Update `:focus` state border to use `var(--primary)`
    - Add placeholder styling with `var(--text-muted)`
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_
  
  - [ ] 5.3 Update modal buttons and alerts
    - Modify `.auth-submit` to use `var(--primary)` for background
    - Update button text to use `var(--background)`
    - Update `:hover` state to use `var(--primary-dark)`
    - Modify `.auth-error` to use dark-theme-compatible error colors
    - Modify `.auth-success` to use dark-theme-compatible success colors
    - Update `.auth-close` to use `var(--text-muted)` with hover to `var(--text)`
    - _Requirements: 6.1, 7.5, 7.6_

- [ ] 6. Update Landing Page CTA and footer sections
  - [ ] 6.1 Update CTA section styling
    - Modify `.cta-section` gradient to use `var(--primary)`, `var(--primary-light)`, and lighter tints
    - Update `.cta-container h2` to use `var(--text)`
    - Update `.cta-container p` to use `var(--text)`
    - Modify `.cta-button` to use `var(--surface)` for background
    - Update `.cta-button` text to use `var(--primary)`
    - _Requirements: 10.3_
  
  - [ ] 6.2 Update footer styling
    - Modify `.landing-footer` to use darker shade (#0A0F1A) for background
    - Update `.footer-text` to use `var(--text-muted)` with reduced opacity
    - Ensure footer logo remains visible
    - Update any footer links to use `var(--text-muted)` with `var(--primary)` on hover
    - _Requirements: 14.1, 14.2, 14.4, 14.6_

- [ ] 7. Update Main Page navigation and hero sections
  - [ ] 7.1 Update top navigation styling
    - Modify `.top-nav` to use `var(--surface)` for background
    - Update border-bottom to use `var(--border)`
    - Update `.user-name` to use `var(--text)`
    - Update `.user-email` to use `var(--text-muted)`
    - Maintain `.logout-btn` with `var(--danger)` background
    - _Requirements: 2.1, 2.2, 6.5_
  
  - [ ] 7.2 Update main page hero section
    - Modify `.uber-hero` gradient to use `var(--primary)`, `var(--primary-light)`, and lighter tints
    - Update `.uber-title` to use `var(--text)`
    - Update `.uber-subtitle` to use `var(--text)`
    - _Requirements: 3.1, 3.2_
  
  - [ ] 7.3 Update stat cards in hero
    - Modify `.stat-card` to use `var(--surface)` for background
    - Update border to use `var(--border)`
    - Update `.stat-number` to use `var(--primary)`
    - Update `.stat-label` to use `var(--text-muted)`
    - Update hover state border to use `var(--primary)`
    - _Requirements: 4.1, 4.3_

- [ ] 8. Update Main Page input and form components
  - [ ] 8.1 Update input card styling
    - Modify `.uber-input-card` to use `var(--surface)` for background
    - Update `.uber-label` to use `var(--text)`
    - Update `.input-header h3` to use `var(--text)`
    - _Requirements: 4.1, 5.2_
  
  - [ ] 8.2 Update input fields
    - Modify `.uber-input` to use `var(--surface)` for background
    - Update input text color to use `var(--text)`
    - Update border to use `var(--border)`
    - Update `:hover` state border to use `var(--primary-light)`
    - Update `:focus` state border to use `var(--primary)`
    - Add placeholder styling with `var(--text-muted)`
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_
  
  - [ ] 8.3 Update search info alert
    - Modify `.search-info` to use dark-theme-compatible background
    - Update text color to use `var(--primary)` or `var(--text)`
    - Update border to complement dark theme
    - _Requirements: 7.6_

- [ ] 9. Update Main Page map components
  - [ ] 9.1 Update map container styling
    - Modify `.uber-map-side` to use `var(--surface)` for background
    - Update border to use `var(--border)`
    - Update `.uber-map-header h2` to use `var(--text)`
    - _Requirements: 8.1, 8.4_
  
  - [ ] 9.2 Update map legend
    - Modify `.uber-legend-item` to use `var(--background)` for background
    - Update text color to use `var(--text-muted)`
    - Update hover state to use `var(--surface)` for background
    - _Requirements: 8.4_
  
  - [ ] 9.3 Update custom map popup styling
    - Modify `.custom-popup .leaflet-popup-content-wrapper` to use `var(--surface)` for background
    - Update border to use `var(--primary)`
    - Update text color to use `var(--text)`
    - Update `.custom-popup .leaflet-popup-tip` to match wrapper styling
    - _Requirements: 8.3_

- [ ] 10. Update Main Page prediction and zone components
  - [ ] 10.1 Update zone list buttons
    - Modify `.uber-zone-button` to use `var(--surface)` for background
    - Update border to use `var(--border)`
    - Update `.uber-zone-name` to use `var(--text)`
    - Update `:hover` state border to use `var(--primary)`
    - Update `:hover` state background to use `var(--surface-hover)`
    - Update `.uber-zone-button::before` accent to use `var(--primary)`
    - _Requirements: 4.1, 4.3_
  
  - [ ] 10.2 Update prediction cards
    - Modify `.uber-prediction-card` to use `var(--surface)` for background
    - Update border-left to use `var(--border)` for default state
    - Update `.uber-card-time` to use `var(--text)`
    - Update `.uber-card-number` to use `var(--text)`
    - Update `.uber-card-label` to use `var(--text-muted)`
    - Update `.uber-card-sub` to use `var(--text-muted)`
    - _Requirements: 9.1, 9.3, 9.4_
  
  - [ ] 10.3 Update prediction card hover states and badges
    - Modify `.uber-prediction-card:hover` border-left-color to use `var(--primary)`
    - Update hover background to use `var(--surface-hover)`
    - Ensure `.uber-card-badge` colors (high/medium/low) remain visible in dark theme
    - Adjust badge colors if needed for contrast
    - _Requirements: 9.2, 9.5_
  
  - [ ] 10.4 Update predictions header
    - Modify `.uber-predictions-header h2` to use `var(--text)`
    - Update `.uber-confidence` to use `var(--primary)`
    - Update header border-bottom to use `var(--border)`
    - _Requirements: 9.3_

- [ ] 11. Update Main Page loading and empty states
  - [ ] 11.1 Update loading states
    - Modify `.uber-spinner` border to use `var(--border)`
    - Update spinner border-top-color to use `var(--primary)`
    - Update `.uber-loading p` to use `var(--text-muted)`
    - _Requirements: 13.4_
  
  - [ ] 11.2 Update skeleton loaders
    - Modify `.skeleton` gradient to use `var(--border)` and `var(--border-light)`
    - Update `.skeleton-card` to use `var(--surface)` for background
    - Update skeleton card border to use `var(--border)`
    - _Requirements: 13.4_
  
  - [ ] 11.3 Update empty state
    - Modify `.uber-empty-state h3` to use `var(--text)`
    - Update `.uber-empty-state p` to use `var(--text-muted)`
    - _Requirements: 4.4_

- [ ] 12. Update Main Page alert and detail components
  - [ ] 12.1 Update alert styling
    - Modify `.uber-alert` to use dark-theme-compatible background
    - Update border to use `var(--warning)` or appropriate semantic color
    - Update `.uber-alert h4` to use `var(--text)`
    - Update `.uber-alert p` to use `var(--text-muted)`
    - _Requirements: 7.6_
  
  - [ ] 12.2 Update details side panel
    - Modify `.uber-details-side` to use `var(--surface)` for background
    - Ensure all text within uses appropriate color variables
    - _Requirements: 4.1_

- [ ] 13. Update responsive styles and media queries
  - [ ] 13.1 Review and update mobile breakpoint styles (max-width: 768px)
    - Verify all color variables are maintained in mobile styles
    - Ensure no hardcoded colors override the theme
    - Test navigation, hero, cards, and forms on mobile
    - _Requirements: 12.1, 12.2_
  
  - [ ] 13.2 Review and update tablet breakpoint styles (769px to 1024px)
    - Verify all color variables are maintained in tablet styles
    - Ensure consistent dark theme appearance
    - Test all components at tablet sizes
    - _Requirements: 12.1, 12.2_
  
  - [ ] 13.3 Review and update desktop breakpoint styles (1025px+)
    - Verify all color variables are maintained in desktop styles
    - Ensure no layout changes affect color visibility
    - Test all components at various desktop sizes
    - _Requirements: 12.1, 12.2_

- [ ] 14. Checkpoint - Visual review and contrast validation
  - Review all pages in browser to verify dark theme appearance
  - Use browser DevTools to inspect color values
  - Run automated contrast checker (axe DevTools or Lighthouse)
  - Verify all text is readable and all interactive elements are visible
  - Test hover, focus, and active states for all interactive elements
  - Ensure all tests pass, ask the user if questions arise
  - _Requirements: 11.1, 11.2, 11.3, 11.6_

- [ ]* 15. Write CSS parsing unit tests
  - [ ]* 15.1 Write test to verify all required CSS variables are defined in :root
    - Test that `--background`, `--surface`, `--primary`, `--text`, and all other required variables exist
    - Test in both LandingPage.css and MainPage.css
    - _Requirements: 15.1_
  
  - [ ]* 15.2 Write test to verify no hardcoded colors outside :root
    - Parse CSS files and find all color values
    - Verify all colors outside :root use var() references
    - **Property 15: CSS Variable Usage Exclusivity**
    - **Validates: Requirements 15.3**
  
  - [ ]* 15.3 Write test to verify all original CSS class names are preserved
    - Compare class names in original and updated CSS files
    - Ensure no classes were removed or renamed
    - **Property 16: CSS Class Name Backward Compatibility**
    - **Validates: Requirements 15.4**
  
  - [ ]* 15.4 Write test to verify specific components use correct variables
    - Test navigation uses var(--surface) for background
    - Test cards use var(--surface) for background
    - Test inputs use var(--surface) for background
    - Test buttons use var(--primary) for background
    - _Requirements: 2.1, 4.1, 5.1, 6.1_

- [ ]* 16. Write contrast ratio property tests
  - [ ]* 16.1 Write property test for universal contrast compliance
    - Generate all text/background color combinations from the color scheme
    - Calculate contrast ratio for each combination
    - Verify all combinations meet WCAG AA standards (4.5:1 for normal text, 3:1 for large text)
    - Run with minimum 100 iterations
    - **Property 1: Universal Contrast Compliance**
    - **Validates: Requirements 3.5, 5.6, 6.6, 8.5, 9.6, 10.2, 10.5, 11.1, 11.2, 11.5**
  
  - [ ]* 16.2 Write property test for button text readability
    - Generate button background colors (primary, danger, secondary)
    - Calculate contrast ratio between button text and background
    - Verify all button text meets 4.5:1 minimum ratio
    - Run with minimum 100 iterations
    - **Property 10: Button Text Readability**
    - **Validates: Requirements 6.2**
  
  - [ ]* 16.3 Write property test for footer link visibility
    - Calculate contrast ratio between footer link color and footer background
    - Verify footer links meet minimum contrast requirements
    - Run with minimum 100 iterations
    - **Property 17: Footer Link Visibility**
    - **Validates: Requirements 14.5**

- [ ]* 17. Write component consistency property tests
  - [ ]* 17.1 Write property test for card background consistency
    - Parse CSS for all card-related classes
    - Verify all cards use var(--surface) for background
    - Run with minimum 100 iterations
    - **Property 2: Card Component Background Consistency**
    - **Validates: Requirements 4.1**
  
  - [ ]* 17.2 Write property test for card hover state primary color accent
    - Parse CSS for all card :hover states
    - Verify all interactive cards use var(--primary) in hover styling
    - Run with minimum 100 iterations
    - **Property 3: Card Hover State Primary Color Accent**
    - **Validates: Requirements 4.3**
  
  - [ ]* 17.3 Write property test for card text color consistency
    - Parse CSS for all card text elements
    - Verify all card text uses var(--text) or var(--text-muted)
    - Run with minimum 100 iterations
    - **Property 4: Card Text Color Consistency**
    - **Validates: Requirements 4.4**
  
  - [ ]* 17.4 Write property test for input field background consistency
    - Parse CSS for all input-related classes
    - Verify all inputs use var(--surface) for background
    - Run with minimum 100 iterations
    - **Property 5: Input Field Background Consistency**
    - **Validates: Requirements 5.1**
  
  - [ ]* 17.5 Write property test for input text color consistency
    - Parse CSS for all input text and label elements
    - Verify all use var(--text)
    - Run with minimum 100 iterations
    - **Property 6: Input Text Color Consistency**
    - **Validates: Requirements 5.2**
  
  - [ ]* 17.6 Write property test for input focus state primary color border
    - Parse CSS for all input :focus states
    - Verify all use var(--primary) for border-color
    - Run with minimum 100 iterations
    - **Property 7: Input Focus State Primary Color Border**
    - **Validates: Requirements 5.3**
  
  - [ ]* 17.7 Write property test for input placeholder muted color
    - Parse CSS for all ::placeholder pseudo-elements
    - Verify all use var(--text-muted)
    - Run with minimum 100 iterations
    - **Property 8: Input Placeholder Muted Color**
    - **Validates: Requirements 5.5**
  
  - [ ]* 17.8 Write property test for primary button background consistency
    - Parse CSS for all primary button classes
    - Verify all use var(--primary) for background
    - Run with minimum 100 iterations
    - **Property 9: Primary Button Background Consistency**
    - **Validates: Requirements 6.1**
  
  - [ ]* 17.9 Write property test for button hover state visual feedback
    - Parse CSS for all button :hover states
    - Verify all include both color change and transform effect
    - Run with minimum 100 iterations
    - **Property 11: Button Hover State Visual Feedback**
    - **Validates: Requirements 6.3**

- [ ]* 18. Write interactive state and responsive property tests
  - [ ]* 18.1 Write property test for interactive element state distinguishability
    - Parse CSS for all interactive elements (buttons, links, inputs, cards)
    - Verify all have distinct :hover, :focus, or :active states
    - Verify states differ from default through color, border, transform, or shadow
    - Run with minimum 100 iterations
    - **Property 12: Interactive Element State Distinguishability**
    - **Validates: Requirements 11.3, 11.6**
  
  - [ ]* 18.2 Write property test for responsive color scheme consistency
    - Parse CSS for all media query blocks
    - Verify no color variables are overridden in media queries
    - Verify color scheme remains consistent across all breakpoints
    - Run with minimum 100 iterations
    - **Property 13: Responsive Color Scheme Consistency**
    - **Validates: Requirements 12.1, 12.2, 12.4, 12.6**
  
  - [ ]* 18.3 Write property test for animation timing preservation
    - Parse CSS for all animation and transition properties
    - Compare timing, duration, and easing functions to original CSS
    - Verify only color values changed, not timing properties
    - Run with minimum 100 iterations
    - **Property 14: Animation Timing Preservation**
    - **Validates: Requirements 13.1, 13.2, 13.3, 13.5**

- [ ] 19. Final checkpoint - Comprehensive testing and validation
  - Run all unit tests and property tests
  - Perform visual regression testing (compare before/after screenshots)
  - Test on multiple browsers (Chrome, Firefox, Safari, Edge)
  - Test on multiple devices (mobile, tablet, desktop)
  - Run accessibility audit with axe DevTools or Lighthouse
  - Test keyboard navigation and focus indicators
  - Verify all animations and transitions work smoothly
  - Gather feedback from team members
  - Ensure all tests pass, ask the user if questions arise

## Notes

- Tasks marked with `*` are optional testing tasks and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Property tests validate universal correctness properties with minimum 100 iterations
- Unit tests validate specific examples and CSS structure
- Checkpoints ensure incremental validation at key milestones
- All color changes are centralized in CSS variables for easy maintenance
- No JavaScript changes required - this is purely a CSS update
- Existing animations, transitions, and responsive behavior are preserved
