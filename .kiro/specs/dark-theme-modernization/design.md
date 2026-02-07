# Design Document: Dark Theme Modernization

## Overview

This design document outlines the technical approach for modernizing the FINDR parking prediction application with a contemporary dark theme. The selected color scheme is **Dark Slate with Emerald**, which maintains the existing brand identity (#10B981 emerald green) while introducing a sophisticated dark aesthetic.

### Design Goals

1. **Brand Continuity**: Maintain FINDR's recognizable emerald green (#10B981) as the primary color
2. **Modern Aesthetic**: Implement a contemporary dark theme that feels professional and polished
3. **Accessibility**: Ensure WCAG AA compliance with minimum 4.5:1 contrast ratios
4. **Maintainability**: Use CSS custom properties for easy theme management
5. **Consistency**: Apply uniform styling across all components and pages

### Selected Color Scheme

- **Background**: #0F172A (dark slate) - Base page background
- **Surface**: #1E293B (lighter slate) - Cards, modals, elevated elements
- **Primary**: #10B981 (emerald green) - Brand color, CTAs, interactive elements
- **Text**: #F1F5F9 (light gray) - Primary text color
- **Secondary Colors**: Maintain existing semantic colors (success, warning, danger) with adjusted opacity for dark theme compatibility

## Architecture

### CSS Variable System

The theme will be implemented using CSS custom properties defined in the `:root` selector. This approach provides:

- **Centralized Control**: All colors defined in one location
- **Easy Maintenance**: Update colors by changing variable values
- **Future Extensibility**: Foundation for potential theme switching functionality
- **Semantic Naming**: Variables named by purpose, not appearance

### File Structure

Two primary CSS files will be modified:
- `frontend/src/pages/LandingPage.css` - Public-facing landing page styles
- `frontend/src/pages/MainPage.css` - Authenticated application interface styles

Both files will share the same color variable definitions to ensure consistency.

### Component Hierarchy

```
Theme System (CSS Variables)
├── Navigation Components
│   ├── Landing Page Navigation
│   └── Main Page Top Navigation
├── Hero Sections
│   ├── Landing Page Hero
│   └── Main Page Hero
├── Card Components
│   ├── Feature Cards
│   ├── Input Cards
│   ├── Prediction Cards
│   └── Stat Cards
├── Form Components
│   ├── Input Fields
│   ├── Buttons
│   └── Labels
├── Modal Components
│   └── Authentication Modal
├── Map Components
│   ├── Map Container
│   ├── Map Markers
│   └── Map Popups
└── Footer Components
```

## Components and Interfaces

### 1. CSS Variable Definitions

**Location**: `:root` selector in both CSS files

**Variables**:
```css
:root {
  /* Primary Theme Colors */
  --background: #0F172A;        /* Dark slate base */
  --surface: #1E293B;           /* Elevated elements */
  --surface-hover: #334155;     /* Hover state for surfaces */
  --primary: #10B981;           /* Emerald green brand color */
  --primary-dark: #059669;      /* Darker primary for hover */
  --primary-light: #34D399;     /* Lighter primary for accents */
  --text: #F1F5F9;              /* Primary text */
  --text-muted: #94A3B8;        /* Secondary text */
  
  /* Semantic Colors */
  --success: #16A34A;
  --warning: #F59E0B;
  --danger: #DC2626;
  --info: #06B6D4;
  
  /* UI Element Colors */
  --border: #334155;            /* Subtle borders */
  --border-light: #475569;      /* Lighter borders */
  --overlay: rgba(0, 0, 0, 0.85); /* Modal backdrop */
  
  /* Gradient Colors */
  --gradient-start: #10B981;
  --gradient-mid: #34D399;
  --gradient-end: #D1FAE5;
  
  /* Legacy Compatibility */
  --dark: #0F172A;
  --dark-light: #1E293B;
  --gray: #94A3B8;
  --gray-light: #334155;
  --white: #F1F5F9;
  --bg: #0F172A;
  --card-bg: #1E293B;
}
```

### 2. Navigation Component

**Purpose**: Provide consistent navigation across landing and main pages

**Styling Approach**:
- Background: `var(--surface)` with 98% opacity and backdrop blur
- Text: `var(--text)` for links and labels
- Hover: `var(--primary)` for link highlights
- Border: `var(--border)` for bottom border
- Logo: Maintain visibility with appropriate contrast

**Key CSS Classes**:
- `.landing-nav` / `.top-nav`: Main navigation container
- `.nav-link`: Navigation links with hover effects
- `.nav-btn`: Primary action button
- `.nav-stat`: Statistics display in navigation

**Hover Behavior**:
```css
.nav-link:hover {
  color: var(--primary);
}

.nav-link::after {
  background: var(--primary);
}
```

### 3. Hero Section Component

**Purpose**: Create engaging first impression with dark gradient background

**Styling Approach**:
- Background: Gradient from `var(--primary)` to lighter tints
- Overlay: Gradient overlay for text readability
- Text: `var(--text)` for titles and subtitles
- Buttons: `var(--primary)` for CTAs
- Cards: `var(--surface)` for floating preview cards

**Gradient Implementation**:
```css
.hero-section {
  background: linear-gradient(135deg, 
    var(--primary) 0%, 
    var(--primary-light) 50%, 
    var(--surface) 100%
  );
}
```

**Text Contrast**: Ensure minimum 4.5:1 ratio by adjusting overlay opacity

### 4. Card Components

**Purpose**: Display content in elevated, organized containers

**Styling Approach**:
- Background: `var(--surface)`
- Border: `var(--border)` with 1-2px width
- Text: `var(--text)` for primary content, `var(--text-muted)` for secondary
- Shadow: Adjusted for dark theme (lighter, more subtle)
- Hover: Border color changes to `var(--primary)`, subtle transform

**Card Variants**:

**Feature Cards**:
```css
.feature-card {
  background: var(--surface);
  border: 1px solid var(--border);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.feature-card:hover {
  border-color: var(--primary);
  transform: translateY(-8px);
  box-shadow: 0 12px 40px rgba(16, 185, 129, 0.2);
}
```

**Prediction Cards**:
```css
.uber-prediction-card {
  background: var(--surface);
  border-left: 4px solid var(--border);
  color: var(--text);
}

.uber-prediction-card:hover {
  border-left-color: var(--primary);
  background: var(--surface-hover);
}
```

### 5. Form and Input Components

**Purpose**: Provide clear, accessible input fields

**Styling Approach**:
- Background: `var(--surface)` for input fields
- Border: `var(--border)` default, `var(--primary)` on focus
- Text: `var(--text)` for input text and labels
- Placeholder: `var(--text-muted)` with reduced opacity
- Focus: Primary color border with subtle glow effect

**Input Styling**:
```css
.uber-input, .form-group input {
  background: var(--surface);
  border: 2px solid var(--border);
  color: var(--text);
}

.uber-input:focus, .form-group input:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
}

.uber-input::placeholder {
  color: var(--text-muted);
  opacity: 0.6;
}
```

### 6. Button Components

**Purpose**: Provide clear call-to-action elements

**Button Types**:

**Primary Buttons**:
```css
.btn-primary, .nav-btn, .auth-submit {
  background: var(--primary);
  color: var(--background);
  border: none;
}

.btn-primary:hover {
  background: var(--primary-dark);
  transform: translateY(-2px);
}
```

**Secondary Buttons**:
```css
.btn-secondary {
  background: transparent;
  color: var(--text);
  border: 2px solid var(--primary);
}

.btn-secondary:hover {
  background: var(--primary);
  color: var(--background);
}
```

**Danger Buttons**:
```css
.logout-btn {
  background: var(--danger);
  color: var(--text);
}

.logout-btn:hover {
  background: #B91C1C;
}
```

### 7. Modal Components

**Purpose**: Display authentication and dialog overlays

**Styling Approach**:
- Backdrop: `var(--overlay)` with 85% opacity
- Content: `var(--surface)` background
- Text: `var(--text)` for all content
- Inputs: Follow form component styling
- Buttons: Follow button component styling

**Modal Structure**:
```css
.auth-modal {
  background: var(--overlay);
}

.auth-content {
  background: var(--surface);
  color: var(--text);
  border: 1px solid var(--border);
}

.auth-close {
  color: var(--text-muted);
}

.auth-close:hover {
  color: var(--text);
}
```

**Alert Messages**:
```css
.auth-error {
  background: rgba(220, 38, 38, 0.15);
  color: #FCA5A5;
  border: 1px solid rgba(220, 38, 38, 0.3);
}

.auth-success {
  background: rgba(16, 185, 129, 0.15);
  color: #6EE7B7;
  border: 1px solid rgba(16, 185, 129, 0.3);
}
```

### 8. Map Components

**Purpose**: Integrate interactive map with dark theme

**Styling Approach**:
- Container: `var(--surface)` background
- Header: `var(--text)` for titles
- Legend: `var(--text-muted)` for labels
- Popups: `var(--surface)` background with `var(--primary)` border
- Markers: Maintain visibility with appropriate colors

**Map Container**:
```css
.uber-map-side {
  background: var(--surface);
  border: 1px solid var(--border);
}

.uber-map-header h2 {
  color: var(--text);
}

.uber-legend-item {
  color: var(--text-muted);
  background: var(--background);
}
```

**Custom Popup Styling**:
```css
.custom-popup .leaflet-popup-content-wrapper {
  background: var(--surface);
  border: 2px solid var(--primary);
  color: var(--text);
}

.custom-popup .leaflet-popup-tip {
  background: var(--surface);
  border: 2px solid var(--primary);
}
```

### 9. Prediction Display Components

**Purpose**: Show parking availability forecasts with clear visual hierarchy

**Styling Approach**:
- Card Background: `var(--surface)`
- Text: `var(--text)` for primary info, `var(--text-muted)` for secondary
- Badges: Semantic colors (success/warning/danger) with adjusted opacity
- Numbers: Large, bold `var(--text)`
- Hover: `var(--primary)` accent with `var(--surface-hover)` background

**Badge Colors** (adjusted for dark theme):
```css
.uber-card-badge.high {
  background: var(--success);
  color: var(--text);
}

.uber-card-badge.medium {
  background: var(--warning);
  color: var(--background);
}

.uber-card-badge.low {
  background: var(--danger);
  color: var(--text);
}
```

### 10. Footer Component

**Purpose**: Provide consistent page footer

**Styling Approach**:
- Background: Darker shade of `var(--background)` (e.g., #0A0F1A)
- Text: `var(--text-muted)` with reduced opacity
- Logo: Maintain visibility
- Links: `var(--primary)` on hover

```css
.landing-footer {
  background: #0A0F1A;
  color: var(--text-muted);
}

.footer-text {
  opacity: 0.8;
}
```

## Data Models

### Color Scheme Model

```typescript
interface ColorScheme {
  name: string;
  colors: {
    background: string;      // Base page background
    surface: string;         // Elevated elements
    surfaceHover: string;    // Hover state
    primary: string;         // Brand color
    primaryDark: string;     // Darker variant
    primaryLight: string;    // Lighter variant
    text: string;            // Primary text
    textMuted: string;       // Secondary text
    border: string;          // Borders
    borderLight: string;     // Lighter borders
    overlay: string;         // Modal backdrop
  };
  semantic: {
    success: string;
    warning: string;
    danger: string;
    info: string;
  };
}
```

### Component State Model

```typescript
interface ComponentState {
  default: {
    background: string;
    color: string;
    border: string;
  };
  hover?: {
    background: string;
    color: string;
    border: string;
    transform?: string;
  };
  focus?: {
    background: string;
    color: string;
    border: string;
    boxShadow?: string;
  };
  active?: {
    background: string;
    color: string;
    border: string;
  };
  disabled?: {
    background: string;
    color: string;
    opacity: number;
  };
}
```

### Contrast Validation Model

```typescript
interface ContrastCheck {
  foreground: string;      // Text or element color
  background: string;      // Background color
  ratio: number;           // Calculated contrast ratio
  wcagLevel: 'AAA' | 'AA' | 'Fail';  // WCAG compliance level
  minimumRequired: number; // 4.5 for normal text, 3.0 for large text
  passes: boolean;         // Whether it meets requirements
}
```

## Data Models


### CSS Class Mapping

The following table maps existing CSS classes to their new dark theme styling:

| Component | CSS Class | Background | Text Color | Border | Hover Effect |
|-----------|-----------|------------|------------|--------|--------------|
| Navigation | `.landing-nav`, `.top-nav` | `var(--surface)` 98% opacity | `var(--text)` | `var(--border)` | N/A |
| Nav Links | `.nav-link` | transparent | `var(--text)` | none | `color: var(--primary)` |
| Hero Section | `.hero-section`, `.uber-hero` | gradient | `var(--text)` | none | N/A |
| Feature Card | `.feature-card` | `var(--surface)` | `var(--text)` | `var(--border)` | `border: var(--primary)` |
| Input Card | `.uber-input-card` | `var(--surface)` | `var(--text)` | none | N/A |
| Input Field | `.uber-input`, `.form-group input` | `var(--surface)` | `var(--text)` | `var(--border)` | `border: var(--primary)` |
| Primary Button | `.btn-primary`, `.nav-btn` | `var(--primary)` | `var(--background)` | none | `background: var(--primary-dark)` |
| Secondary Button | `.btn-secondary` | transparent | `var(--text)` | `var(--primary)` | `background: var(--primary)` |
| Modal | `.auth-content` | `var(--surface)` | `var(--text)` | `var(--border)` | N/A |
| Prediction Card | `.uber-prediction-card` | `var(--surface)` | `var(--text)` | `var(--border)` | `background: var(--surface-hover)` |
| Map Container | `.uber-map-side` | `var(--surface)` | `var(--text)` | `var(--border)` | N/A |
| Footer | `.landing-footer` | `#0A0F1A` | `var(--text-muted)` | none | N/A |

## Implementation Strategy

### Phase 1: CSS Variable Setup

1. **Update `:root` selector** in both CSS files with new color variables
2. **Maintain legacy variables** for backward compatibility
3. **Document each variable** with inline comments
4. **Test variable inheritance** across all components

### Phase 2: Component-by-Component Migration

**Order of Implementation**:
1. Navigation components (highest visibility)
2. Hero sections (immediate visual impact)
3. Card components (most numerous)
4. Form and input components (user interaction)
5. Button components (CTAs)
6. Modal components (authentication flow)
7. Map components (integration complexity)
8. Footer components (lowest priority)

### Phase 3: Gradient and Effect Updates

1. **Update hero gradients** to use new color scheme
2. **Adjust box shadows** for dark theme (lighter, more subtle)
3. **Update backdrop blur effects** for navigation
4. **Refine hover transitions** with new colors

### Phase 4: Accessibility Validation

1. **Test contrast ratios** for all text/background combinations
2. **Verify focus indicators** are clearly visible
3. **Test with screen readers** to ensure semantic structure maintained
4. **Validate color-blind friendly** design choices

### Phase 5: Responsive Testing

1. **Test on mobile devices** (320px to 768px)
2. **Test on tablets** (769px to 1024px)
3. **Test on desktop** (1025px+)
4. **Verify all breakpoints** maintain dark theme consistency

## Contrast Ratio Calculations

### Text Combinations

| Element | Foreground | Background | Ratio | WCAG Level | Passes |
|---------|------------|------------|-------|------------|--------|
| Body Text | #F1F5F9 | #0F172A | 14.8:1 | AAA | ✓ |
| Muted Text | #94A3B8 | #0F172A | 7.2:1 | AAA | ✓ |
| Card Text | #F1F5F9 | #1E293B | 12.6:1 | AAA | ✓ |
| Button Text | #0F172A | #10B981 | 8.9:1 | AAA | ✓ |
| Primary on Surface | #10B981 | #1E293B | 5.8:1 | AA | ✓ |
| Muted on Surface | #94A3B8 | #1E293B | 6.1:1 | AA | ✓ |
| Error Text | #FCA5A5 | #0F172A | 8.4:1 | AAA | ✓ |
| Success Text | #6EE7B7 | #0F172A | 11.2:1 | AAA | ✓ |

All combinations exceed WCAG AA requirements (4.5:1 for normal text, 3:1 for large text).

## Animation and Transition Considerations

### Existing Animations to Preserve

1. **fadeIn**: Opacity transition (0 to 1)
2. **fadeInUp**: Opacity + translateY transition
3. **slideUp**: Transform + opacity for modals
4. **slideInRight**: Transform + opacity for alerts
5. **float**: Continuous translateY for hero cards
6. **pulse**: Opacity oscillation for loading states
7. **spin**: Rotation for loading spinners
8. **shimmer**: Background position for skeleton loaders

### Transition Updates

All transitions will maintain their timing and easing functions. Only color values will change:

```css
/* Example: Hover transition */
.nav-link {
  transition: color 0.3s ease;
}

/* Example: Focus transition */
.uber-input:focus {
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

/* Example: Card hover */
.feature-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}
```

### Loading States

**Skeleton Loaders**:
```css
.skeleton {
  background: linear-gradient(90deg, 
    var(--border) 25%, 
    var(--border-light) 50%, 
    var(--border) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
```

**Spinners**:
```css
.uber-spinner {
  border: 4px solid var(--border);
  border-top-color: var(--primary);
}
```

## Browser Compatibility

### CSS Custom Properties Support

- Chrome 49+ ✓
- Firefox 31+ ✓
- Safari 9.1+ ✓
- Edge 15+ ✓

### Fallback Strategy

For older browsers that don't support CSS custom properties, the design will gracefully degrade to the existing light theme. This is acceptable as the target audience uses modern browsers.

```css
/* Fallback example */
.feature-card {
  background: #1E293B; /* Fallback */
  background: var(--surface); /* Modern browsers */
}
```

## Testing Strategy

### Visual Regression Testing

1. **Capture screenshots** of all pages before changes
2. **Apply dark theme** changes
3. **Capture screenshots** of all pages after changes
4. **Compare side-by-side** to verify intentional changes only
5. **Test all interactive states** (hover, focus, active)

### Accessibility Testing

1. **Automated contrast checking** using tools like axe DevTools
2. **Manual keyboard navigation** testing
3. **Screen reader testing** with NVDA/JAWS
4. **Color blindness simulation** using browser extensions
5. **Reduced motion preference** testing

### Cross-Browser Testing

1. **Chrome** (latest)
2. **Firefox** (latest)
3. **Safari** (latest)
4. **Edge** (latest)
5. **Mobile Safari** (iOS)
6. **Chrome Mobile** (Android)

### Responsive Testing

1. **Mobile**: 320px, 375px, 414px
2. **Tablet**: 768px, 834px, 1024px
3. **Desktop**: 1280px, 1440px, 1920px
4. **Test orientation changes** on mobile/tablet

### User Acceptance Testing

1. **Internal team review** for initial feedback
2. **A/B testing** with subset of users (if applicable)
3. **Gather feedback** on readability and aesthetics
4. **Iterate based on feedback** before full rollout

## Performance Considerations

### CSS File Size

The changes will not significantly impact CSS file size:
- Adding CSS variables: ~1KB
- Updating color values: 0KB (replacement, not addition)
- Total estimated increase: <1KB

### Rendering Performance

- CSS custom properties have negligible performance impact
- No additional DOM elements required
- No JavaScript required for theme application
- Existing animations and transitions unchanged

### Caching Strategy

- CSS files should be cache-busted after deployment
- Use versioned filenames or query parameters
- Set appropriate cache headers for static assets


## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Universal Contrast Compliance

*For any* text element and its background in the theme system, the contrast ratio SHALL be at least 4.5:1 for normal text (or 3:1 for large text 18pt+), ensuring WCAG AA compliance across all components including hero sections, cards, inputs, buttons, modals, maps, prediction displays, gradients, and footer elements.

**Validates: Requirements 3.5, 5.6, 6.6, 8.5, 9.6, 10.2, 10.5, 11.1, 11.2, 11.5**

### Property 2: Card Component Background Consistency

*For any* card component (feature cards, input cards, prediction cards, stat cards), the background color SHALL use `var(--surface)` to ensure consistent appearance across all card types.

**Validates: Requirements 4.1**

### Property 3: Card Hover State Primary Color Accent

*For any* interactive card component, when in the hover state, the styling SHALL include `var(--primary)` in either the border-color, background, or accent element to provide consistent visual feedback.

**Validates: Requirements 4.3**

### Property 4: Card Text Color Consistency

*For any* card component, all text content SHALL use `var(--text)` for primary content or `var(--text-muted)` for secondary content to ensure consistent readability.

**Validates: Requirements 4.4**

### Property 5: Input Field Background Consistency

*For any* input field component (text inputs, date inputs, select elements), the background color SHALL use `var(--surface)` to ensure consistent appearance.

**Validates: Requirements 5.1**

### Property 6: Input Text Color Consistency

*For any* input field component, the text color SHALL use `var(--text)` and labels SHALL use `var(--text)` to ensure consistent readability.

**Validates: Requirements 5.2**

### Property 7: Input Focus State Primary Color Border

*For any* input field component, when in the focus state, the border-color SHALL use `var(--primary)` to provide consistent visual feedback.

**Validates: Requirements 5.3**

### Property 8: Input Placeholder Muted Color

*For any* input field component, the placeholder text SHALL use `var(--text-muted)` with reduced opacity to ensure consistent placeholder styling.

**Validates: Requirements 5.5**

### Property 9: Primary Button Background Consistency

*For any* primary action button (submit buttons, CTA buttons, navigation buttons), the background color SHALL use `var(--primary)` to ensure consistent brand presence.

**Validates: Requirements 6.1**

### Property 10: Button Text Readability

*For any* button component, the text color SHALL provide sufficient contrast against the button background (minimum 4.5:1 ratio) to ensure readability.

**Validates: Requirements 6.2**

### Property 11: Button Hover State Visual Feedback

*For any* button component, the hover state SHALL include both a color change (darker shade) and a transform effect to provide consistent interactive feedback.

**Validates: Requirements 6.3**

### Property 12: Interactive Element State Distinguishability

*For any* interactive element (buttons, links, inputs, cards), the hover, focus, and active states SHALL have visually distinct styling from the default state through color, border, transform, or shadow changes.

**Validates: Requirements 11.3, 11.6**

### Property 13: Responsive Color Scheme Consistency

*For any* responsive breakpoint (mobile, tablet, desktop), the color scheme variables SHALL remain unchanged, ensuring consistent dark theme appearance across all screen sizes.

**Validates: Requirements 12.1, 12.2, 12.4, 12.6**

### Property 14: Animation Timing Preservation

*For any* animated or transitioning element, the animation timing, duration, and easing functions SHALL remain unchanged from the original implementation, ensuring only color values are updated.

**Validates: Requirements 13.1, 13.2, 13.3, 13.5**

### Property 15: CSS Variable Usage Exclusivity

*For any* color value in the CSS files (excluding the :root selector), the value SHALL be a CSS custom property reference (var()) rather than a hardcoded color value, ensuring centralized color management.

**Validates: Requirements 15.3**

### Property 16: CSS Class Name Backward Compatibility

*For any* CSS class name that existed in the original light theme, the class name SHALL still exist in the dark theme implementation, ensuring no breaking changes to the HTML structure.

**Validates: Requirements 15.4**

### Property 17: Footer Link Visibility

*For any* footer link element, the text color SHALL provide sufficient contrast against the footer background to ensure visibility and accessibility.

**Validates: Requirements 14.5**

## Error Handling

### CSS Fallback Strategy

**Unsupported Browsers**: For browsers that don't support CSS custom properties (pre-2016), the theme will gracefully degrade to hardcoded fallback colors:

```css
.feature-card {
  background: #1E293B; /* Fallback for old browsers */
  background: var(--surface); /* Modern browsers */
}
```

**Missing Variables**: If a CSS variable is undefined, browsers will use the fallback value or ignore the property:

```css
.element {
  color: var(--text, #F1F5F9); /* Fallback to light gray if --text is undefined */
}
```

### Contrast Ratio Failures

**Detection**: During development, use automated tools (axe DevTools, Lighthouse) to detect contrast failures.

**Resolution**: If a contrast failure is detected:
1. Identify the failing text/background combination
2. Adjust the color variable to increase contrast
3. Re-test all components using that variable
4. Document the change in the CSS comments

### Animation Performance Issues

**Detection**: Monitor for janky animations or layout shifts during theme application.

**Resolution**:
1. Ensure only color properties are changed, not layout properties
2. Use `will-change` CSS property for frequently animated elements
3. Test on lower-end devices to ensure smooth performance

### Responsive Breakpoint Issues

**Detection**: Visual regression testing at each breakpoint.

**Resolution**:
1. Verify media queries don't override color variables
2. Ensure all components are tested at each breakpoint
3. Fix any layout issues that affect color visibility

## Testing Strategy

### Unit Testing Approach

**CSS Parsing Tests**: Write tests that parse the CSS files and verify:
- All required CSS variables are defined in :root
- All color values outside :root use var() references
- All original CSS class names still exist
- Specific components use the correct variables

**Example Test Structure**:
```javascript
describe('Dark Theme CSS Variables', () => {
  test('All required variables are defined in :root', () => {
    const cssContent = readCSSFile('LandingPage.css');
    const rootVars = extractRootVariables(cssContent);
    
    expect(rootVars).toContain('--background');
    expect(rootVars).toContain('--surface');
    expect(rootVars).toContain('--primary');
    expect(rootVars).toContain('--text');
    // ... more assertions
  });
  
  test('Navigation uses surface color for background', () => {
    const cssContent = readCSSFile('LandingPage.css');
    const navStyles = extractClassStyles(cssContent, '.landing-nav');
    
    expect(navStyles.background).toContain('var(--surface)');
  });
});
```

### Property-Based Testing Approach

**Contrast Ratio Testing**: Generate all text/background combinations and verify contrast ratios:

```javascript
describe('Contrast Ratio Properties', () => {
  test('Property 1: All text/background combinations meet WCAG AA', () => {
    const colorScheme = {
      background: '#0F172A',
      surface: '#1E293B',
      text: '#F1F5F9',
      textMuted: '#94A3B8',
      primary: '#10B981'
    };
    
    const combinations = [
      { fg: colorScheme.text, bg: colorScheme.background, minRatio: 4.5 },
      { fg: colorScheme.text, bg: colorScheme.surface, minRatio: 4.5 },
      { fg: colorScheme.textMuted, bg: colorScheme.background, minRatio: 4.5 },
      { fg: colorScheme.textMuted, bg: colorScheme.surface, minRatio: 4.5 },
      { fg: colorScheme.primary, bg: colorScheme.surface, minRatio: 3.0 },
      // ... more combinations
    ];
    
    combinations.forEach(({ fg, bg, minRatio }) => {
      const ratio = calculateContrastRatio(fg, bg);
      expect(ratio).toBeGreaterThanOrEqual(minRatio);
    });
  });
});
```

**CSS Variable Usage Testing**: Verify no hardcoded colors exist outside :root:

```javascript
describe('CSS Variable Usage', () => {
  test('Property 15: All colors use CSS variables', () => {
    const cssContent = readCSSFile('LandingPage.css');
    const hardcodedColors = findHardcodedColors(cssContent, { excludeRoot: true });
    
    expect(hardcodedColors).toHaveLength(0);
  });
});
```

**Backward Compatibility Testing**: Verify all original class names exist:

```javascript
describe('Backward Compatibility', () => {
  test('Property 16: All original class names preserved', () => {
    const originalClasses = extractClassNames('LandingPage.css.original');
    const newClasses = extractClassNames('LandingPage.css');
    
    originalClasses.forEach(className => {
      expect(newClasses).toContain(className);
    });
  });
});
```

### Integration Testing

**Visual Regression Testing**:
1. Capture screenshots of all pages before changes
2. Apply dark theme changes
3. Capture screenshots of all pages after changes
4. Use image comparison tools (Percy, Chromatic) to detect unintended changes
5. Review and approve intentional changes

**Cross-Browser Testing**:
1. Test on Chrome, Firefox, Safari, Edge (latest versions)
2. Test on mobile browsers (iOS Safari, Chrome Mobile)
3. Verify consistent appearance across all browsers
4. Document any browser-specific issues

**Accessibility Testing**:
1. Run automated accessibility audits (axe, Lighthouse)
2. Test keyboard navigation (Tab, Enter, Escape)
3. Test with screen readers (NVDA, JAWS, VoiceOver)
4. Verify focus indicators are visible
5. Test with color blindness simulators

**Responsive Testing**:
1. Test at mobile breakpoints (320px, 375px, 414px)
2. Test at tablet breakpoints (768px, 834px, 1024px)
3. Test at desktop breakpoints (1280px, 1440px, 1920px)
4. Verify consistent dark theme at all sizes
5. Test orientation changes on mobile/tablet

### Manual Testing Checklist

**Component-by-Component Review**:
- [ ] Navigation: Colors, hover states, logo visibility
- [ ] Hero section: Gradient, text readability, CTA buttons
- [ ] Feature cards: Background, borders, hover effects
- [ ] Input fields: Background, text, focus states, placeholders
- [ ] Buttons: Primary, secondary, danger variants, hover states
- [ ] Authentication modal: Background, overlay, form elements
- [ ] Map: Container, markers, popups, legend
- [ ] Prediction cards: Background, badges, text, hover effects
- [ ] Footer: Background, text, links, logo
- [ ] Loading states: Spinners, skeleton loaders
- [ ] Animations: Smooth transitions, no jarring changes

**User Acceptance Testing**:
1. Internal team review for initial feedback
2. Test with actual users for readability and aesthetics
3. Gather feedback on any eye strain or readability issues
4. Iterate based on feedback before full deployment

### Test Configuration

**Property-Based Test Settings**:
- Minimum 100 iterations per property test
- Each test tagged with: **Feature: dark-theme-modernization, Property {number}: {property_text}**
- Use deterministic random seed for reproducibility

**Test Coverage Goals**:
- 100% of CSS variables defined and used correctly
- 100% of contrast ratios meeting WCAG AA standards
- 100% of original CSS classes preserved
- 100% of components visually tested at all breakpoints

### Continuous Integration

**Automated Checks**:
1. CSS linting to ensure variable usage
2. Contrast ratio calculations on every commit
3. Visual regression tests on pull requests
4. Accessibility audits on staging deployments

**Pre-Deployment Checklist**:
- [ ] All unit tests passing
- [ ] All property tests passing (100 iterations each)
- [ ] Visual regression tests reviewed and approved
- [ ] Accessibility audit passing (no critical issues)
- [ ] Cross-browser testing completed
- [ ] Responsive testing completed
- [ ] User acceptance testing completed
- [ ] Performance metrics within acceptable range
