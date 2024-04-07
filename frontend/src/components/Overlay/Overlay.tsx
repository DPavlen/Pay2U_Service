import './Overlay.scss'
import { MouseEventHandler, ReactElement } from 'react';

interface OverlayProps {
  isMenuOpen: boolean;
  handleMenuOpen: MouseEventHandler<HTMLDivElement>;
}

function Overlay(props: OverlayProps): ReactElement {
  return (
    <div onClick={props.handleMenuOpen} className={`overlay ${props.isMenuOpen ? 'overlay_active' : ''}`}/>
  );
}

export default Overlay;
