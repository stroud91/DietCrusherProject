import React from 'react';

const Svg = ({ children, size = 20, strokeWidth = 1.8, fill = 'none', ...rest }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill={fill} stroke="currentColor"
    strokeWidth={strokeWidth} strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" {...rest}>
    {children}
  </svg>
);

export const SearchIcon = (p) => <Svg {...p}><circle cx="11" cy="11" r="7" /><path d="m20 20-3.5-3.5" /></Svg>;
export const BagIcon = (p) => <Svg {...p}><path d="M6 7h12l1 13H5L6 7Z" /><path d="M9 7a3 3 0 0 1 6 0" /></Svg>;
export const UserIcon = (p) => <Svg {...p}><circle cx="12" cy="8" r="4" /><path d="M4 21a8 8 0 0 1 16 0" /></Svg>;
export const HomeIcon = (p) => <Svg {...p}><path d="m3 11 9-7 9 7" /><path d="M5 10v10h14V10" /></Svg>;
export const ReceiptIcon = (p) => <Svg {...p}><path d="M6 3h12v18l-3-2-3 2-3-2-3 2V3Z" /><path d="M9 8h6M9 12h6" /></Svg>;
export const HeartIcon = ({ filled, ...p }) => (
  <Svg {...p} fill={filled ? 'currentColor' : 'none'}>
    <path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z" />
  </Svg>
);
export const StarIcon = ({ filled = true, ...p }) => (
  <Svg {...p} fill={filled ? 'currentColor' : 'none'} strokeWidth={1.4}>
    <path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9L12 3Z" />
  </Svg>
);
export const PlusIcon = (p) => <Svg {...p}><path d="M12 5v14M5 12h14" /></Svg>;
export const MinusIcon = (p) => <Svg {...p}><path d="M5 12h14" /></Svg>;
export const CloseIcon = (p) => <Svg {...p}><path d="M6 6l12 12M18 6 6 18" /></Svg>;
export const ChevronRight = (p) => <Svg {...p}><path d="m9 6 6 6-6 6" /></Svg>;
export const ChevronLeft = (p) => <Svg {...p}><path d="m15 6-6 6 6 6" /></Svg>;
export const ClockIcon = (p) => <Svg {...p}><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></Svg>;
export const BikeIcon = (p) => <Svg {...p}><circle cx="6" cy="17" r="3" /><circle cx="18" cy="17" r="3" /><path d="M6 17 9 9h5l4 8M12 9l-1-3H9" /></Svg>;
export const PinIcon = (p) => <Svg {...p}><path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12Z" /><circle cx="12" cy="9" r="2.5" /></Svg>;
export const PhoneIcon = (p) => <Svg {...p}><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z" /></Svg>;
export const ShareIcon = (p) => <Svg {...p}><path d="M12 3v12M7 8l5-5 5 5" /><path d="M5 13v7h14v-7" /></Svg>;
export const EditIcon = (p) => <Svg {...p}><path d="M4 20h4L19 9l-4-4L4 16v4Z" /></Svg>;
export const TrashIcon = (p) => <Svg {...p}><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3" /></Svg>;
export const StoreIcon = (p) => <Svg {...p}><path d="M4 9 5.5 4h13L20 9M4 9h16v11H4V9Z" /><path d="M10 20v-6h4v6" /></Svg>;
export const SunIcon = (p) => <Svg {...p}><circle cx="12" cy="12" r="4" /><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4" /></Svg>;
export const MoonIcon = (p) => <Svg {...p}><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5Z" /></Svg>;
export const CheckIcon = (p) => <Svg {...p}><path d="m5 12 5 5L20 7" /></Svg>;
export const TagIcon = (p) => <Svg {...p}><path d="M3 12V4h8l10 10-8 8L3 12Z" /><circle cx="7.5" cy="8.5" r="1.5" /></Svg>;
export const LogoutIcon = (p) => <Svg {...p}><path d="M15 4h4v16h-4M10 17l5-5-5-5M15 12H3" /></Svg>;
export const FlameIcon = (p) => <Svg {...p}><path d="M12 21a6 6 0 0 0 6-6c0-4-3-6-4-9-2 2-2 4-2 5-1-1-2-2-2-4-2 2-4 5-4 8a6 6 0 0 0 6 6Z" /></Svg>;
export const ChartIcon = (p) => <Svg {...p}><path d="M4 20V10M10 20V4M16 20v-7M22 20H2" /></Svg>;
